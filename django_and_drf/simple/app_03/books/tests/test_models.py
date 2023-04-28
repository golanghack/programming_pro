from django.test import TestCase 
from books.models import Author, Book

class TestModels(TestCase):

    def test_book_has_an_author(self):
        book = Book.objects.create(title='The lord of the rings')
        tolkin = Author.objects.create(first_name='John', last_name='Tolkin')
        rouling = Author.objects.create(first_name='Joan', last_name='Rouling')
        book.authors.set([tolkin.pk, rouling.pk])

        self.assertEqual(book.authors.count(), 2)

    
    def test_author_has_an_book(self):
        book = Book.objects.create(title='The lord of the rings')
        tolkin = Author.objects.create(first_name='John', last_name='Tolkin')
        rouling = Author.objects.create(first_name='Joan', last_name='Rouling')
        tolkin.book_set.add(book)
        rouling.book_set.add(book)

        self.assertEqual(book.authors.count(), 2)


    def test_model_str(self):
        book = Book.objects.create(title='The Lord of the Rings.')
        tolkin = Author.objects.create(first_name='John', last_name='Tolkien')

        self.assertEqual(str(book), 'The Lord of the Rings.')
        self.assertEqual(str(tolkin), 'John Tolkien')
