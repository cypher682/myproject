

# Create your tests here.
from django.test import TestCase
from .models import Task

class TaskModelTests(TestCase):
    def test_task_creation(self):
        task = Task.objects.create(title="Test Task", description="Test Description")
        self.assertEqual(task.title, "Test Task")
        self.assertFalse(task.completed)
