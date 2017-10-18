from django.test import TestCase
from .models import TodoList, TodoListItem, User


class TodoListTestCase(TestCase):
    def setUp(self):
        self.todo_list = TodoList.objects.create(name='Test list', user=User.objects.create())

    def test_completed(self):
        self.assertTrue(self.todo_list.completed())


class TodoListItemTestCase(TestCase):
    def setUp(self):
        self.todo_list_item = TodoListItem.objects.create(
            title='Test item',
            todo_list=TodoList.objects.create(name='Test list', user=User.objects.create()),
            text='Lorem ipsum dolor ... sit amet'
        )

    def test_done(self):
        self.assertFalse(self.todo_list_item.done)
