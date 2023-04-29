from django.forms import ModelForm
from django.forms import Textarea
from .models import Contact

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'message',]
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': 'Talking about H.Potter.'
                }
            )
        }