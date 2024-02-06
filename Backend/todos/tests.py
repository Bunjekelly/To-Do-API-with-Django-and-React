from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='Do ALX tasks', body='you have many pending tasks')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_name = f'{todo.title}'
        self.assertEqual(expected_name, 'Do ALX tasks')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_name = f'{todo.body}'
        self.assertEqual(expected_name, 'you have many pending tasks')