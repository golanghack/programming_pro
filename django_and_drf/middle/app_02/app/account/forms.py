from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Enter user name')
    password = forms.CharField(label='Enter password', widget=forms.PasswordInput)

