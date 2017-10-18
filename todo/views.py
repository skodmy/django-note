# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import TodoList, TodoListItem


class TodoListListView(LoginRequiredMixin, ListView):
    model = TodoList
    context_object_name = 'todo_lists'
    template_name = 'todo_lists_list.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TodoListItemListView(LoginRequiredMixin, ListView):
    model = TodoListItem
    context_object_name = 'todo_list_items'
    template_name = 'todo_list_items_list.html'

    def get_queryset(self):
        return self.model.objects.filter(todo_list__id=int(self.kwargs['todo_list_id']))

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['todo_list'] = TodoList.objects.get(id=self.kwargs['todo_list_id'])
        return context_data


class TodoListItemDetailView(DetailView):
    model = TodoListItem
    template_name = 'todo_list_item_detail.html'
