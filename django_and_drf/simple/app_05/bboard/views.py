from django.http import HttpResponse

def index(request: str) -> HttpResponse:
    return HttpResponse('Hi')