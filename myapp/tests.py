

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoTests(TestCase):
    def test_todo_list_page(self):
        Todo.objects.create(task="Test Task")
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Task")
