from django.http import HttpResponse

from .models import Pizza

def index(request: str, pid: int) -> HttpResponse:
    pizza = Pizza.objects.get(id=pid)
    return HttpResponse(
        content={
            'id': pizza.id, 
            'title': pizza.title,
            'description': pizza.description,
        }
    )
