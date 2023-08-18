from django.http import HttpResponse

def home(request: str) -> HttpResponse:
    return HttpResponse('Hello')