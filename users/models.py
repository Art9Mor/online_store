from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Почта', unique=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=35, verbose_name='Страна', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
