from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    # path('save_profiles/', views.member,name='save_profiles'),
    path('login/', views.login_now, name="login"),
    # path('classify/', views.member, name="classify"),
    path('search/', views.search, name="search"),
    path('category/', views.category, name="category"),
    path('logout/', views.logout_now, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('detail/', views.detail, name="detail"),
    path('checkout/', views.checkout, name="checkout"),
    # path('update_item/', views.home, name="update_item"),
    
]