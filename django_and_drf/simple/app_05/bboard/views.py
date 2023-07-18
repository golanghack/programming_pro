from django.shortcuts import render
from bboard.models import Bb, Rubric


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)
def index(request: str):
    bbs = Bb.objects.all()
    return render(request, 'bboard/base.html', {'bbs': bbs})
    