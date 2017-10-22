# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import TodoList, TodoListItem


class Index(LoginRequiredMixin, ListView):
    model = TodoList
    context_object_name = 'todo_lists'
    template_name = 'todo/index.html'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


class CRUDViewCommonMixin:
    model = None
    pk_url_kwarg = ''
    context_object_name = ''


class TodoListCRUDViewCommonMixin(CRUDViewCommonMixin):
    model = TodoList
    pk_url_kwarg = 'todo_list_id'
    context_object_name = 'todo_list'


class TodoListCreateView(LoginRequiredMixin, TodoListCRUDViewCommonMixin, CreateView):
    fields = ['name']
    template_name = 'todo/list/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoListDetailView(LoginRequiredMixin, TodoListCRUDViewCommonMixin, DetailView):
    template_name = 'todo/list/detail.html'


class TodoListUpdateView(LoginRequiredMixin, TodoListCRUDViewCommonMixin, UpdateView):
    fields = ['name']
    template_name = 'todo/list/update.html'


class TodoListDeleteView(LoginRequiredMixin, TodoListCRUDViewCommonMixin, DeleteView):
    template_name = 'todo/list/delete.html'
    success_url = reverse_lazy('todo:index')


class TodoListItemCRUDViewCommonMixin(CRUDViewCommonMixin):
    model = TodoListItem
    pk_url_kwarg = 'todo_list_item_id'
    context_object_name = 'todo_list_item'


class TodoListItemCreateView(LoginRequiredMixin, TodoListItemCRUDViewCommonMixin, CreateView):
    fields = ['title', 'text']
    template_name = 'todo/list/item/create.html'

    def form_valid(self, form):
        form.instance.todo_list = TodoList.objects.get(id=self.kwargs['todo_list_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo:list-detail', kwargs=self.kwargs)


class TodoListItemDetailView(LoginRequiredMixin, TodoListItemCRUDViewCommonMixin, DetailView):
    template_name = 'todo/list/item/detail.html'


class TodoListItemUpdateView(LoginRequiredMixin, TodoListItemCRUDViewCommonMixin, UpdateView):
    fields = ['title', 'text', 'done']
    template_name = 'todo/list/update.html'

    def get_success_url(self):
        return reverse('todo:list-detail', kwargs={'todo_list_id': self.kwargs['todo_list_id']})


class TodoListItemDeleteView(LoginRequiredMixin, TodoListItemCRUDViewCommonMixin, DeleteView):
    template_name = 'todo/list/delete.html'

    def get_success_url(self):
        return reverse('todo:list-detail', kwargs={'todo_list_id': self.kwargs['todo_list_id']})
