from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from typing import Union


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