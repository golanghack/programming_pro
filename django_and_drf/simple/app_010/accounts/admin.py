from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.forms import MyUserChangeForm, MyUserCreationForm

MyUser = get_user_model()

class MyUserAdmin(MyUser):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser
    list_display = ['email', 'username']

admin.site.register(MyUser, MyUserAdmin)
