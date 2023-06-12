from django import forms

class ItemForm(forms.Form):
    """-> for element of list form """

    item_text = forms.CharField(
        widget=forms.fields.TextInput(attrs={
            'placeholder':'Enter a to-do',
            'class': 'form-control input-lg',
        }),
    )
