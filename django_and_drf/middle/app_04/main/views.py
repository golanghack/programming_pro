from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import (LoginView, LogoutView, 
                                        PasswordChangeView)
from django.views.generic.edit import (UpdateView, CreateView, DeleteView)
from django.views.generic.base import TemplateView
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView)
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.signing import BadSignature
from django.core.paginator import Paginator
from django.db.models import Q 
from django.contrib.auth import logout
from django.contrib import messages
from typing import Union, Callable

from main.models import (AdvUser, SubRubric, 
                        News)
from main.forms import (ChangeUserInfoForm, RegisterUserForm,
                        SearchForm, NewsForm, AddImageSet)
from main.utils import signer

def index(request: str) -> render:
    news = News.objects.filter(is_active=True)[:10]
    context = {'news': news}
    return render(request, 'main/index.html', context)

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

    news = News.objects.filter(author=request.user.pk)
    context = {'news': news}
    return render(request, 'main/profile.html', context)

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


def user_activate(request: str, sign: str) -> render:
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'main/bad_signature.html')
    
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'main/user_is_activated.html'
    else:
        template = 'main/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    """Delete user view""" 

    model = AdvUser
    template_name = 'main/delete_user.html'
    success_url = reverse_lazy('main:index')

    def setup(self, request: str, *args, **kwargs) -> Callable:
        self.user_id = request.user.pk 
        return super().setup(request, *args, **kwargs)

    def post(self, request: str, *args, **kwargs) -> Callable:
        logout(request)
        messages.add_message(request, messages.SUCCESS, 
                                'Пользователь  успешно удален')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset: str=None) -> get_object_or_404:
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class AppPasswordResetView(PasswordResetView):
    template_name = 'main/password_reset.html'
    subject_template_name = 'email/reset_letter_subject.txt'
    email_template_name = 'email/reset_letter_body.txt'
    success_url = reverse_lazy('main:password_reset_done')

class AppPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'main/password_reset_done.html'

class AppPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'main/password_confirm.html'
    success_url = reverse_lazy('main:password_reset_complete')

class AppPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'main/password_complete.html'


def by_rubric(request: str, pk: int) -> render:
    """Serching news on rubric with keywords argument in GET""" 

    rubric = get_object_or_404(SubRubric, pk=pk)
    news = News.objects.filter(is_active=True, rubric=pk)
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(title__icontains=keyword) | Q(content__icontains=keyword)
        news = news.filter(q)
    else:
        keyword = ''
    
    form = SearchForm(initial={
        'keyword': keyword
    })
    paginator = Paginator(news, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1 
    page = paginator.get_page(page_num)
    context = {
        'rubric': rubric, 
        'page': page,
        'news': page.object_list,
        'form': form
    }
    return render(request, 'main/by_rubric.html', context)
    

def detail(request: str, rubric_pk: int, pk: int) -> render:
    """Render detail for rubric pk""" 

    new = get_object_or_404(News, pk=pk)
    ais = new.additionalimage_set.all()
    context = {
        'new': new, 
        'ais': ais
    }
    return render(request, 'main/detail.html', context)

@login_required
def profile_new_detail(request: str, pk: int) -> render or redirect:
    """Render detail for rubric pk""" 

    new = get_object_or_404(News, pk=pk)
    ais = new.additionalimage_set.all()
    context = {
        'new': new, 
        'ais': ais
    }
    return render(request, 'main/profile_new_detail.html', context)

@login_required
def profile_news_add(request: str) -> redirect:
    """Controller for add news from user""" 

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save()
            formset = AddImageSet(request.POST, request.FILES, instance=new)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Новость добавлена')
                return redirect('main:profile')
    else:
        form = NewsForm(initial={'author': request.user.pk})
        formset = AddImageSet()
    context = {'form': form, 'formset': formset}
    return render(request, 'main/profile_news_add.html', context)

@login_required
def profile_news_change(request: str, pk: int) -> render or redirect:
    """User change of news""" 

    new = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=new)
        if form.is_valid():
            new = form.save()
            formset = AddImageSet(request.POST, request.FILES, instance=new)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Новость исправлена')
                return redirect('main:profile')
    else:
        form = NewsForm(instance=new)
        formset = AddImageSet(instance=new)
    context = {'form': form, 'formset': formset}

    return render(request, 'main/profile_news_change.html', context)

@login_required
def profile_news_delete(request: str, pk: int) -> redirect or render:
    """News delete""" 

    new = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        new.delete()
        messages.add_message(request, messages.SUCCESS, 'Новость удалена')
        return redirect('main:profile')
    else:
        context = {'new': new}
        return render(request, 'main/profile_news_delete.html', context)