from django.http import HttpResponse
from bboard.models import Bb

def index(request: str) -> HttpResponse:
    list_board = 'List of boards\r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        list_board += bb.title + '\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(list_board, content_type='text/plain; charset=utf-8')