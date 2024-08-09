from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import UserCreationForm
# Create your views here.

#Biến tổng
user_not_login = 'visible'
user_login = 'hidden'

def home(request):
    context = {
        'user_not_login': user_not_login, 
        'user_login': user_login
    }
    return render(request, 'app/home.html',context)

def login_now(request):
    global user_login
    global user_not_login
    if request.user.is_authenticated:
        context = {
        'user_not_login': user_not_login, 
        'user_login': user_login
        }
        return render(request, 'app/home.html', context)
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password =password)
        if user is not None :
            user_not_login = 'hidden'
            user_login = 'visible'
            context = {
                'user_not_login': user_not_login, 
                'user_login': user_login
            }
            login(request,user)
            return render(request,'app/home.html',context)
        else:
            messages.info(request, 'Tài khoản hoặc mật khẩu không chính xác!')
    
    user_not_login = 'visibile'
    user_login = 'hidden'
    context = {
        'user_not_login': user_not_login, 
        'user_login': user_login
    }
    return render(request,'app/login.html',context)

def logout_now(request):
    
    logout(request)
    user_not_login = 'visibile'
    user_login = 'hidden'
    context = {
        'user_not_login': user_not_login, 
        'user_login': user_login
    }
    return render(request, 'app/home.html', context)

def register(request):
    global user_login
    global user_not_login
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Đăng nhập người dùng ngay sau khi đăng ký thành công (tuỳ chọn)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            # Lưu thông tin người dùng vào session
            request.session['user_id'] = user.id
            user_not_login = 'hidden'
            user_login = 'visibile'
            context = {
                'user': username,
                'user_login':user_login, 
                'user_not_login':user_not_login
                }
            return render(request,'app/home.html',context)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Lỗi ở trường '{form.fields[field].label}': {error}")
    user_not_login = "visibile"
    user_login = "hidden"
    context = {
        'form': form,
        'user_login':user_login,
        'user_not_login':user_not_login
    }
    return render(request, 'app/register.html', context)

def search(request):
    context = {
        'user_not_login': user_not_login, 
        'user_login': user_login
    }
    return render(request, 'app/search.html',context)

def category(request):
    return render(request, 'app/category.html')

def checkout(request):
    context = {
        'user_not_login': user_not_login, 
        'user_login': user_login
    }
    return render(request, 'app/checkout.html',context)

def detail(request):
    return render(request, 'app/detail.html')

def cart(request):
    context = {
        'user_not_login': user_not_login, 
        'user_login': user_login
    }
    return render(request, 'app/cart.html', context)

def staff(request):
    context = {
        'user_not_login': user_not_login, 
        'user_login': user_login
    }
    
    return render(request, 'app/staff.html', context)

def profile(request):
    context = {
        'user_not_login': user_not_login, 
        'user_login': user_login
    }
    
    return render(request, 'app/staff.html', context)