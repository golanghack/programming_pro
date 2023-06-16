from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from lists.models import Item, List

def home(request):
    
    return render(request, 'home.html')

def view_list(request, my_list_id):
    """View of list"""
    
    my_list = List.objects.get(id=my_list_id)
    error = None
    if request.method == 'POST':
        try:
            item = Item.objects.create(text=request.POST['item_text'], my_list=my_list)
            item.full_clean()
            item.save()
            return redirect(my_list)
        except ValidationError:
            error = 'You can`t have an empty list item'
    
    return render(request, 'list.html', {
        'my_list': my_list,
    })

def new_list(request):
    """-> new list"""

    form = ItemForm(data=request.POST)
    if form.is_valid():
        my_list = List()
        my_list.owner = request.user
        my_list.save()
        form.save(for_my_list=my_list)
        return redirect(my_list)
    else:
        return render(request, 'home.html', {'form': form})

def add_item(request, list_id):
    """Add new item in list"""

    my_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], my_list=my_list, item_text=True)
    return redirect(f'/lists/{my_list.id}/')