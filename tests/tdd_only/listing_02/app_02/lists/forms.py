from django import forms

class ItemForm(forms.Form):
    """-> for element of list form """

    item_text = forms.CharField()
    