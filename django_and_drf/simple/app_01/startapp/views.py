from django.shortcuts import render
from .models import AppDb, Rubric

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