from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.

# Django Shell
user = User.objects.get(username='minh6')
user.is_staff = False
user.save()

# Kiểm tra nhóm
print(user.groups.all())  # Đảm bảo rằng nhóm 'Staff' đã được thêm
