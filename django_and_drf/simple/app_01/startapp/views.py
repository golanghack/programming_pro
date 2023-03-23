from django.shortcuts import render
from .models import AppDb

def index(request: str) -> str:
    
    boards = AppDb.objects.order_by('-published')
    return render(request, 'startapp/index.html', {'boards': boards})