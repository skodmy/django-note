"""
todo app models goes here.
"""
from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    """
    A class that represents a user's todo list.
    """
    user = models.ForeignKey(User)
    name = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    @property
    def completed(self):
        """
        Checks if all items for self are checked.

        :return: True if all are True, False otherwise.
        """
        return all((todo_list_item.checked for todo_list_item in TodoListItem.objects.filter(todo_list=self)))

    def __str__(self):
        return '{}, created: {}, modified: {}'.format(
            self.name,
            self.created,
            self.modified
        )


class TodoListItem(models.Model):
    """
    A class which objects represent todo list items.
    """
    todo_list = models.ForeignKey(TodoList)
    title = models.CharField(max_length=150)
    text = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return '{} from {} is {}'.format(self.title, self.todo_list.name, 'done' if self.done else 'undone')
