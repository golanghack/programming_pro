from django.shortcuts import render, redirect
from .models import Item

def home_page(request):

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/unic_list/')
    items = Item.objects.all()
    return render(request, 'base.html', {'items': items})

def view_list(request):
    """View of list"""

    items = Item.objects.all()
    return render(request, 'base.html', {'items': items})

