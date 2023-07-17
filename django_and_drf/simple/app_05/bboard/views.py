from django.http import HttpResponse
from django.template import loader
from bboard.models import Bb

def index(request: str) -> HttpResponse:
    template = loader.get_template('bboard/base.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))