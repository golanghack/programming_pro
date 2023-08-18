from django import forms
from django.utils.translation import gettext_lazy as _

# counters for choice for user quantity
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 101)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=_("Quantity")
    )
    override = forms.BooleanField(
        required=False, initial=False, widget=forms.HiddenInput
    )
