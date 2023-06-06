from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, 
                                    product=item['product'],
                                    price=item['price'],
                                    quantity=item['quantity'],)
            cart.clear()
            # start async tasks with celery
            order_created.delay(order.id)
            
            # order in seance
            request.session['order_id'] = order.id 
            # edirect to pay
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {
        'cart': cart, 'form': form,
    })
