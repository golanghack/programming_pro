from django.shortcuts import render, redirect
from lists.models import Item

def home(request):
    
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    
    return render(request, 'home.html')
