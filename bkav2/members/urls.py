from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import api1


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login_now, name="login"),
    path('search/', views.search, name="search"),
    path('category/', views.category, name="category"),
    path('logout/', views.logout_now, name="logout"),
    path('cart/', views.cart, name="cart"),
    path('detail/', views.detail, name="detail"),
    path('checkout/', views.checkout, name="checkout"),
    path('staff/', views.staff, name = 'staff'),
    path('profile/', views.profile, name = 'profile'),
    path('ordercheck/', views.profile, name = 'ordercheck'),
    path('update_item/', views.update_item, name="update_item"),
    path('api/users/', api1.as_view() , name='user-list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
