from django.test import TestCase
from todos.models import Todo

class TodoTest(TestCase):
    
    @classmethod
    def setUpTestData(cls: str):
        Todo.objects.create(title='one test', body='one test')

    def test_title_correct(self):
        todo = Todo.objects.get(id=1)
        expected_name = f'{todo.title}'
        self.assertEqual(expected_name, 'one test')

    def test_body_correct(self):
        todo = Todo.objects.get(id=1)
        expected_name = f'{todo.body}'
        self.assertEqual(expected_name, 'one test')