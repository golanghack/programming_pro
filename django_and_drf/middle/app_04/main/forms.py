from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
from typing import Callable

from main.apps import user_registered 
from main.models import (AdvUser, SuperRubric, 
                        SubRubric, News, 
                        AdditionalImage, Comment)

class ChangeUserInfoForm(forms.ModelForm):
    """Change`s forms for email""" 

    email = forms.EmailField(required=True,
                            label='Адрес электронной почты')
    class Meta:
        model = AdvUser
        # dont changes parameters ->
        fields = ('username', 'email', 'first_name', 'last_name', 'send_messages')


class RegisterUserForm(forms.ModelForm):
    """Form for user registration""" 

    email = forms.EmailField(required=True, 
                                label='Адрес електронной почты')
    password1 = forms.CharField(label='Пароль', 
                                widget=forms.PasswordInput,
                                help_text=password_validation.password_validators_help_text_html())
    password2 = forms.CharField(label='Пароль (повторно)',
                                widget=forms.PasswordInput,
                                help_text='Введите пароль еще раз')
    
    def clean_password1(self) -> password1:
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self) -> Callable:
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError(
                'Введенные вами пароли не совпадают', code='password_mismatch'
            )}
            raise ValidationError(errors)
    
    def save(self, commit: bool=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = False
        user.is_activated = False

        if commit:
            user.save()
        user_registered.send(RegisterUserForm, instance=user)
        return user 
    
    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'password1', 'password2', 
                    'first_name', 'last_name', 'send_messages')


class SubRubricForm(forms.ModelForm):
    super_rubric = forms.ModelChoiceField(
        queryset=SuperRubric.objects.all(),
        empty_label=None,
        label='Родительская рубрика',
        required=True
    )

    class Meta:
        model = SubRubric
        fields = '__all__'
        

class SearchForm(forms.Form):
    """Form for serach on site""" 

    keyword = forms.CharField(required=False, 
                                max_length=30, 
                                label='')

class NewsForm(forms.ModelForm):
    """Form for added news for user"""

    class Meta:
        model = News
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}

AddImageSet = inlineformset_factory(News, AdditionalImage, fields='__all__')


class UserCommentForm(forms.ModelForm):
    """Comment form for user""" 

    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'new': forms.HiddenInput}


class AnonCommentForm(forms.ModelForm):
    """Comment form for anonymouse user""" 

    captcha = CaptchaField(label='Введите текст с картинки',
                            error_messages={'invalid': 'Неверно'})
    
    class Meta:
        model = Comment
        exclude = ('is_active',)
        widgets = {'new': forms.HiddenInput}