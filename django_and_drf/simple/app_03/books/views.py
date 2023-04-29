from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import ContactForm

class ContactBuilder(CreateView):

    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('correct')

def correct(request):
    return HttpResponse('Hello! Thanks!')