# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User,Group
from .models import Profile,Staff
from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    
    if created :
        # Trong trường hợp tạo User mới 
        if not instance.is_staff:
            Profile.objects.create(user=instance)
            
    else:
        # Trong trường hợp cập nhật User
        if instance.is_staff:
            # Nếu đây là thêm staff 
            if not Staff.objects.filter(user=instance).exists():
                Staff.objects.create(user=instance)
            Profile.objects.filter(user=instance).delete()
        else:
            # Nếu đây là xóa Staff
            if Staff.objects.filter(user=instance).exists():
                Staff.objects.filter(user=instance).delete()
            if not Profile.objects.filter(user=instance).exists():
                Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    user = instance
    def add_group(group_name):
        group = Group.objects.get(name = group_name)
        user.groups.add(group)
        
    def del_group(group_name):
        group = Group.objects.get(name = group_name)
        user.groups.remove(group)
        
    if created :
        # Trong trường hợp tạo User mới 
        if not instance.is_staff:
            add_group('Customer')
    else:
        # Trong trường hợp cập nhật User
        if instance.is_staff:
            # Nếu đây là thêm staff 
            if not user.groups.filter(name='Staff').first():
                add_group('Staff')
            del_group('Customer')
        else:
            # Nếu đây là xóa Staff
            if user.groups.filter(name='Staff').first():
                del_group('Staff')
            if not user.groups.filter(name='Customer').first():
                add_group('Customer')
