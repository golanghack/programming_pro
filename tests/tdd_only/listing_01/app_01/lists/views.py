from django.shortcuts import redirect, render
from lists.models import Item, List

def home(request):
    
    return render(request, 'home.html')

def view_list(request):
    """View of list"""

    items = Item.objects.all()
    return render(request, 'list.html', {
        'items': items,
    })

def new_list(request):
    """-> new list""" 

    my_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], my_list=my_list)
    return redirect('/lists/one/')