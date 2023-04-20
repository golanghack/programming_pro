from django.shortcuts import render
from .models import Item

def home_page(request):
    
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save()
    return render(request, 'base.html', {
        'new_item_text': item.text,
    })
