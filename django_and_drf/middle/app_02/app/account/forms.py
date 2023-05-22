from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(label='Enter user name')
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email',]

    # validation fields
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\`t mattc')
        return cd['password2']


    def clean_email(self):
        """Realisation unic email for user registration""" 

        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Error alredy in use.')
        return data 

        


class UserEditForm(forms.ModelForm):

    class Meta:

        model = User
        fields = ['first_name', 'last_name', 'email',]

    def clean_email(self):
        """Validation email for used email another user"""
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)

        if qs.exists():
            raise forms.ValidationError('Email already in use.')
        return data 

class ProfileEditForm(forms.ModelForm):

    class Meta:

        model = Profile
        fields = ['date_of_birth', 'photo',]