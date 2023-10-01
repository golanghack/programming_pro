from django import forms
from lists.models import Item

class ItemForm(forms.Form):
    """-> for element of list form """

    class Meta:

        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do', 
                'class': 'form-control input-lg',
            }),
        }
form = ItemForm()
print(form)