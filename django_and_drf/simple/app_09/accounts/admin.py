from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.forms import MyUserChangeForm, MyUserCreationForm
from accounts.models import MyUser

MyUser = get_user_model()

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['email', 'username']

admin.site.register(MyUser, MyUserAdmin)