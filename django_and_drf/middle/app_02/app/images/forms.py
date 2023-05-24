from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
import requests
from .models import Image

class ImageCreateForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['title', 'url', 'description',]
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg', 'png',]
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not mathch valid image format.')
        
        return url 

    def save(self, forse_insert: bool=False, force_update: bool=False, commit: bool=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'

        # dowmload
        response = requests.get(image_url)
        image.image.save(image_name, ContentFile(response.content), save=False)

        if commit:
            image.save()
        return image

    