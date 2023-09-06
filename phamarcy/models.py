from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, verbose_name='Name', help_text='Full Name')
    email = models.EmailField(unique=True, max_length=50,  blank=False, null=False, verbose_name='Email')

    def __str__(self) -> str:
        return self.name