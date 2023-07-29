from django import forms
from main.models import AdvUser

class ChangeUserInfoForm(forms.ModelForm):
    """Change`s forms for email""" 

    email = forms.EmailField(required=True,
                            label='Адрес электронной почты')
    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')
