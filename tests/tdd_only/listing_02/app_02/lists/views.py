from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from lists.models import Item, List

def home(request):
    
    return render(request, 'home.html')

def view_list(request, my_list_id):
    """View of list"""
    
    my_list = List.objects.get(id=my_list_id)
    return render(request, 'list.html', {
        'my_list': my_list,
    })

def new_list(request):
    """-> new list""" 

    my_list = List.objects.create()
    item =Item.objects.create(text=request.POST['item_text'], my_list=my_list)
    try:
        item.full_clean()
    except ValidationError:
        error = 'List item dont empty!'
        return render(request, 'home.html', {'error': error})
    return redirect(f'/lists/{my_list.id}/')

def add_item(request, list_id):
    """Add new item in list"""

    my_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], my_list=my_list)
    return redirect(f'/lists/{my_list.id}/')