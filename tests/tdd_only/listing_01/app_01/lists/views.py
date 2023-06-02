from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['item_text'])
    return render(request, 'home.html')
