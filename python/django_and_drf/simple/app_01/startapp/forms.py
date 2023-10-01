from django.forms import ModelForm
from .models import AppDb

class BbForm(ModelForm):

    class Meta:
        model = AppDb
        fields = ('title', 'content', 'price', 'rubric',)
        