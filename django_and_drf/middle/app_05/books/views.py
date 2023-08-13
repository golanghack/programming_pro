from django.views.generic import ListView
from books.models import Book 

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
