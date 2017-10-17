# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Todo, TodoList, TodoListItem


class TodoListView(LoginRequiredMixin, ListView):
    CLS_NAME_SUFFIX = ''
    model = Todo
    # noinspection PyUnresolvedReferences
    template_name = 'todo_{}_list.html'
    context_object_name = 'todo_{}'

    def __init__(self):
        super().__init__()
        self.template_name = self.template_name.format(self.CLS_NAME_SUFFIX)
        self.context_object_name = self.context_object_name.format(self.CLS_NAME_SUFFIX)
        print(self.__dict__)


class TodoListListView(TodoListView):
    CLS_NAME_SUFFIX = 'lists'
    model = TodoList

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class TodoListItemListView(TodoListView):
    CLS_NAME_SUFFIX = 'list_items'
    model = TodoListItem

    def get_queryset(self):
        return self.model.objects.filter(todo_list__id=int(self.kwargs['todo_list_id']))

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['todo_list'] = TodoList.objects.get(id=self.kwargs['todo_list_id'])
        return context_data
