from django.shortcuts import render


def index(request: str) -> render:
    return render(request, 'main/index.html')
