from django.http import HttpResponse

def index(request) -> str:
    return HttpResponse('WOW')
