from django.views.generic import ListView
from books.models import Book

class Books(ListView):
    model = Book
    template_name = 'books/books.html'