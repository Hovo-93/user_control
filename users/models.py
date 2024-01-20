
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(verbose_name='Email', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'