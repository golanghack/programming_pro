from django.http import HttpResponse

def home_page_view(request: str) -> HttpResponse:
    return HttpResponse('Hello')