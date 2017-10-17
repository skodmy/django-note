# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Todo, TodoList, TodoListItem


class TodoListView(LoginRequiredMixin, ListView):
    CLS_NAME_SUFFIX = ''
    model = Todo
    # noinspection PyUnresolvedReferences
    template_name = 'todo_{}_list.html'.format(CLS_NAME_SUFFIX)
    context_object_name = 'todo_{}'.format(CLS_NAME_SUFFIX)


class TodoListListView(TodoListView):
    CLS_NAME_SUFFIX = 'lists'
    model = TodoList
    # noinspection PyUnresolvedReferences
    # template_name = super(TodoListView).template_name.format('lists')
    # context_object_name = super(TodoListView).context_object_name.format('lists')

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TodoListItemListView(TodoListView):
    CLS_NAME_SUFFIX = 'list_items'
    model = TodoListItem
    # noinspection PyUnresolvedReferences
    # template_name = super(TodoListView).template_name.format('list_items')
    # context_object_name = super(TodoListView).context_object_name.format('list_items')

    def get_queryset(self):
        return self.model.objects.filter(todo_list=self.request.todo_list)
