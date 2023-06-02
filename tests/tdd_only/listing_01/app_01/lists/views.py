from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    return render(request, 'home.html', {
        'new_item_text': request.POST['item_text'],
    })
