from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import LessonForm
from app.models import Lesson


class UsersRegistrationView(CreateView):
    template_name = '/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('lessons')

    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        login(self.request, user)
        return result

class UserEnrollLessonView(LoginRequiredMixin, FormView):
    lesson = None
    form_class = LessonForm

    def form_valid(self, form):
        self.lesson = form.cleaned_data['lesson']
        self.lesson.users.add(self.request.user)
        return super().form_valid(form)
    

