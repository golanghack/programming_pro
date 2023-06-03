from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart:

    def __init__(self, request: str) -> None:
        """Cart class initialisation""" 

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # empty
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product: str, quantity: int=1, override_quantity: bool=False) -> None:
        """Added product in cart or update quantity""" 

        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self) -> None:
        """Mark session for changed"""

        self.session.modified = True

    