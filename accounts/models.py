from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Profile(models.Model):
   
    user = models.OneToOneField(get_user_model(),related_name="profile",on_delete=models.CASCADE,verbose_name = "کاربر")
    age = models.IntegerField(verbose_name = "سن")
    gender = models.CharField(max_length=10,verbose_name = "جنسیت")
    bio = models.TextField(verbose_name = "بیوگرافی")
    
    def __str__(self):
        return self.gender

    class Meta:
        verbose_name_plural = "پروفایل ها"
        verbose_name = "پروفایل"