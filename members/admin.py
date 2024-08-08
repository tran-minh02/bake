from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, Permission
from django.contrib.sessions.models import Session
# Register your models here.
class AdminShippingAddress(admin.ModelAdmin):
    list_display = ('customer', 'address', 'mobile')
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(ShippingAddress,AdminShippingAddress)
admin.site.register(Profile)
admin.site.register(Staff)
admin.site.register(Permission)
admin.site.register(Session)