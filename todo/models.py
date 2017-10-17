"""
todo app models goes here.
"""
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    """
    Base abstract model for todo app models.
    """
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} created at {}, last modified at {}'.format(
            self.name,
            self.created_at,
            self.last_modified_at
        )

    class Meta:
        abstract = True


class TodoList(Todo):
    """
    A class that represents a user's todo list.
    """
    user = models.ForeignKey(User)

    def is_completed(self):
        """
        Checks if all items for self are checked.

        :return: True if all are True, False otherwise.
        """
        return all((todo_list_item.checked for todo_list_item in TodoListItem.objects.filter(todo_list=self)))


class TodoListItem(Todo):
    """
    A class which objects represent todo list items.
    """
    todo_list = models.ForeignKey(TodoList)
    text = models.TextField()
    checked = models.BooleanField(default=False)
