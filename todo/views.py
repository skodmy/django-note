from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo, TodoList, TodoListItem


class TodoListView(ListView):
    model = Todo


class TodoListListView(TodoListView):
    model = TodoList


class TodoListItemListView(TodoListView):
    model = TodoListItem
