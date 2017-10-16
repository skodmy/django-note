from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_created=True)
    last_modification_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ToDoListItem(models.Model):
    title = models.CharField(max_length=300)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_created=True)
    last_modification_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
