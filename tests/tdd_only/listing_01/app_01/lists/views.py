from django.shortcuts import redirect, render
from lists.models import Item

def home(request):
    
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/one/')
    items = Item.objects.all()
    return render(request, 'home.html', {
        'items': items,
    })

def view_list(request):
    """View of list"""

    items = Item.objects.all()
    return render(request, 'list.html', {
        'items': items,
    })