from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import AppDb, Rubric
from .forms import BbForm
from typing import Any, Dict

def index(request: str) -> str:
    
    boards = AppDb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'boards': boards, 'rubrics': rubrics}
    return render(request, 'startapp/index.html', context)

def by_rubric(request, rubric_id):
    boards = AppDb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {
        'boards': boards, 
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }
    return render(request, 'startapp/by_rubric.html', context)

class BoardCreateView(CreateView):

    template_name = 'startapp/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context