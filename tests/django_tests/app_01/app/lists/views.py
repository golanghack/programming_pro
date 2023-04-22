from django.shortcuts import render, redirect
from .models import Item

def home_page(request):

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/unic_list/')
    return render(request, 'base.html')

def view_list(request):
    """View of list"""

    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    """New list"""
    
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/unic_list/')
