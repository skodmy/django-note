# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import TodoList, TodoListItem


class TodoListListView(LoginRequiredMixin, ListView):
    model = TodoList
    context_object_name = 'todo_lists'
    template_name = 'todo/lists_list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TodoListDetailView(LoginRequiredMixin, DetailView):
    model = TodoList
    context_object_name = 'todo_list'
    template_name = 'todo/list_detail.html'


class TodoListItemDetailView(LoginRequiredMixin, DetailView):
    model = TodoListItem
    context_object_name = 'todo_list_item'
    template_name = 'todo/list_item_detail.html'
