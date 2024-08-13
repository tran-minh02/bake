from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
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
            return redirect('home')
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
    
    categories = Category.objects.filter(is_sub=False)
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
            return redirect('home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Lỗi ở trường '{form.fields[field].label}': {error}")
    
    context = {
        'form': form,
        'categories': categories
    }
    return render(request, 'app/register.html', context)

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
    
def search(request):
    return render(request, 'app/search.html')

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

def staff(request):
    print(request.user.groups.all())
    if request.user.groups.filter(name='Staff').exists() == False | request.user.groups.filter(name='Admin').exists() == False :
        return redirect('home')
    else:
        pass
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
    categories = Category.objects.filter(is_sub=False)
    user_p = request.user
    if request.method == 'POST':
        user_p.last_name = request.POST.get('lastname')
        user_p.first_name = request.POST.get('firstname')
        profile.birthdate = request.POST.get('birthday')
        user_p.email = request.POST.get('emailname')
        profile.phone_number= request.POST.get('phonename')
        user_p.save()
        profile.save()

    context = {
        'profile' : profile,
        'shipping': shipping,
        'categories':categories
    }
    
    return render(request, 'app/profile.html',context)
from rest_framework.response import Response
class api1(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)