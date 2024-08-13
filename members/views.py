from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .decorator import staff_required
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created =  Order.objects.get_or_create(customer = customer,complete =False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
    else:
        items =[]
        order = {'get_cart_items':0, 'get_cart_tatol':0}
        cartitems = order['get_cart_items']
    products = Product.objects.all()
    categories = Category.objects.filter(is_sub=False)
    context= {
        'products': products,
        'categories' : categories
              }
    print(request.user.groups.all())
    return render(request, 'app/home.html',context)

def login_now(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password =password)
        if user is not None :
            login(request,user)
            return render(request,'app/home.html')
        else:
            messages.info(request, 'Tài khoản hoặc mật khẩu không chính xác!')
    categories = Category.objects.filter(is_sub =False)
    context = {
        'categories': categories
    }
    return render(request,'app/login.html',context)

def logout_now(request):
    logout(request)
    return redirect('home')

def register(request):
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
            context = {
                'user': username
                }
            return render(request,'app/home.html',context)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Lỗi ở trường '{form.fields[field].label}': {error}")
    categories = Category.objects.filter(is_sub=False)
    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'app/register.html', context)

def search(request):
    return render(request, 'app/search.html')

def category(request):
    categories = Category.objects.filter(is_sub = False)
    active_category = request.GET.get('category','')
    if active_category:
        products = Product.objects.filter(category__slug = active_category)
        if request.user.is_authenticated:
            customer = request.user
            order, created =  Order.objects.get_or_create(customer = customer,complete =False)
            items = order.orderitem_set.all()
            cartitems = order.get_cart_items
        else:
            items = []
            order = {'get_cart_items':0, 'get_cart_tatol':0}
            cartitems = order['get_cart_items']
    context = {
        'cartitems': cartitems,
        'categories': categories, 
        'products': products, 
        'active_category': active_category
        }
    return render(request,'app/category.html',context)
    

def checkout(request):
    categories = Category.objects.filter(is_sub=False)
    context = {
        'categories':categories
    }
    return render(request, 'app/checkout.html',context)

def detail(request):
    categories = Category.objects.filter(is_sub=False)
    context = {
        'categories':categories
    }
    return render(request, 'app/detail.html',context)

def cart(request):
    categories = Category.objects.filter(is_sub=False)
    context = {
        'categories':categories
    }
    return render(request, 'app/cart.html', context)

@staff_required
def staff(request):
    context = {
        
    }
    return render(request, 'app/staff.html', context)

def ordercheck(request):
    context = {
        
    }
    
    return render(request, 'app/ordercheck.html', context)

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    shipping = ShippingAddress.objects.filter(customer_id = request.user)
    
    # print(request.user)
    print(profile.phone_number)
    # for i in shipping:
    #     print(i.address)
    print(request.user.first_name)
    
    categories = Category.objects.filter(is_sub=False)
    
    context = {
        'profile' : profile,
        'shipping': shipping,
        'categories':categories
    }
    
    return render(request, 'app/profile.html',context)

