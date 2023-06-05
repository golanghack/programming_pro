from django.shortcuts import redirect, render
from lists.models import Item, List

def home(request):
    
    return render(request, 'home.html')

def view_list(request, my_list_id):
    """View of list"""
    my_list = List.objects.get(id=my_list_id)
    items = Item.objects.filter(my_list=my_list)
    return render(request, 'list.html', {
        'items': items,
    })

def new_list(request):
    """-> new list""" 

    my_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], my_list=my_list)
    return redirect(f'/lists/{my_list.id}/')