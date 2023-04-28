from django.test import TestCase 
from books.models import Author, Book, Event
from datetime import datetime

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

    def test_event_model(self):

        event = Event.objects.create(
            title='The Lord of the Rings.'
            seo_title='Some', 
            seo_description='Some desc',
            abstract='The abstract',
            body='The body', 
            duration=2,
            slug='the-slug',
            start_date=datetime.now()
            end_date=datetime.now(),
            price=800,
            location='London',
            published=False,
        )
        