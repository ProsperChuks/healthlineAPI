from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserCreationFormExtended(UserCreationForm): 
    class Meta:
        model = User
        fields = ['email', 'name']

UserAdmin.add_form = UserCreationFormExtended
UserAdmin.add_fieldsets = (
    (None, {
        'fields': ('name', 'email', 'username', 'password1', 'password2',)
    }),
)

# Register your models here.
admin.site.register(User, UserAdmin)
