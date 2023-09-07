import json
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name='Name', help_text='Full Name')
    email = models.EmailField(unique=True, max_length=50, blank=False, null=False, verbose_name='Email')

    def __str__(self) -> str:
        return self.name

class Products(models.Model):
    image = models.ManyToManyField("productImages", blank=True, verbose_name="Product Image")
    drug_name = models.CharField(max_length=600, verbose_name="Drug Name", blank=False, null=False,)
    drug_desc = models.TextField(verbose_name="Drug Description")
    price = models.IntegerField(verbose_name="Price", blank=False, null=False)
    category = models.CharField(max_length=200, verbose_name="Drug Category")
    presentation = models.IntegerField(verbose_name="Presentation", blank=False, null=False,)
    composition = models.TextField(verbose_name="Composition")
    indications = models.JSONField(verbose_name="Indications")

    def __str__(self) -> str:
        return self.drug_name

class productImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, to_field='id')
    images = models.ImageField(upload_to=f"uploads/% Y/% m/% d/{product}", null=True)

    def __str__(self) -> str:
        return str(self.images)

class Checkouts(models.Model):
    name = models.CharField(max_length=200, verbose_name='Name', help_text='Full Name', blank=False, null=False)
    email = models.EmailField(unique=True, max_length=50,  blank=False, null=False, verbose_name='Email')
    phone = models.CharField(max_length=14, verbose_name="Phone Number")
    address = models.TextField(max_length=1000, verbose_name="Home Address")
    state = models.CharField(max_length=40, verbose_name="State")
    lga = models.CharField(max_length=50, verbose_name="Local Government")
    add_info = models.TextField(max_length=200, verbose_name="Additional Information")
