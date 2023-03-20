from django.http import HttpResponse

from .models import AppDb

def index(request: str) -> str:
    announcement_list = 'List of announcement\r\n\r\n\r\n'
    for ann in AppDb.objects.order_by('-published'):
        announcement_list += (ann.title + '\r\n' + ann.content + '\r\n\r\n')
    return HttpResponse(announcement_list, content_type='text/plain; charset=utf-8')
