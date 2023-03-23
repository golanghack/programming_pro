from django.http import HttpResponse
from django.template import loader
from .models import AppDb

def index(request: str) -> str:
    
    template = loader.get_template('startapp/index.html')
    boards = AppDb.objects.order_by('-published')
    context = {'boards': boards}
    return HttpResponse(template.render(context, request))