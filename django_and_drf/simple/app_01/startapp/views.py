from django.shortcuts import render
from .models import AppDb

def index(request: str) -> str:
    
    boards = AppDb.objects.all()
    return render(request, 'startapp/index.html', {'boards': boards})