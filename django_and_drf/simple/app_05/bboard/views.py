from django.shortcuts import render
from bboard.models import Bb

def index(request: str):
    bbs = Bb.objects.order_by('-published')
    return render(request, 'bboard/base.html', {'bbs': bbs})
    