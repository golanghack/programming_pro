from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import (LoginView, LogoutView, 
                                        PasswordChangeView)
from django.views.generic.edit import (UpdateView, CreateView)
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from typing import Union, Callable

from main.models import AdvUser
from main.forms import ChangeUserInfoForm, RegisterUserForm

def index(request: str) -> render:
    return render(request, 'main/index.html')

def other_page(request: str, page: str) -> Union[HttpResponse, Http404]:
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class AppLoginView(LoginView):
    """App Login View""" 

    template_name = 'main/login.html'

@login_required
def profile(request: str) -> render:
    """profile user"""
    return render(request, 'main/profile.html')

class AppLogoutView(LoginRequiredMixin, LogoutView):
    """App logout view""" 

    template_name = 'main/logout.html'


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """Change user data class""" 

    model = AdvUser
    template_name = 'main/change_user_info.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('main:profile')
    success_message = 'Данные успешно изменены'

    def setup(self, request: str, *args, **kwargs) -> Callable:
        self.user_id = request.user.pk 
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset: str=None) -> get_object_or_404:
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class AppPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    """App change password possible""" 

    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Пароль успешно изменен'

class RegisterUserView(CreateView):
    """Registration new user"""

    model = AdvUser
    template_name = 'main/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')

class RegisterDoneView(TemplateView):
    """Register done view""" 

    template_name = 'main/register_done.html'