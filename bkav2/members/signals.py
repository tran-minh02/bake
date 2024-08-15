# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User,Group
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created :
        # Trong trường hợp tạo User mới 
        if not instance.is_staff:
            Profile.objects.create(user=instance)