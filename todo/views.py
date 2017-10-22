# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import TodoList, TodoListItem


class TodoListCreateView(LoginRequiredMixin, CreateView):
    model = TodoList
    fields = ['name']
    template_name = 'todo/list_add.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TodoListUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoList
    fields = ['name']
    template_name = 'todo/list_update.html'


class TodoListDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoList
    template_name = 'todo/list_delete.html'
    success_url = reverse_lazy('todo:index')


class Index(LoginRequiredMixin, ListView):
    model = TodoList
    context_object_name = 'todo_lists'
    template_name = 'todo/index.html'

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


class TodoListItemCreateView(LoginRequiredMixin, CreateView):
    model = TodoListItem
    fields = ['title', 'text']
    context_object_name = 'todo_list_item'
    template_name = 'todo/list_item_add.html'

    def form_valid(self, form):
        form.instance.todo_list = TodoList.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('todo:list-detail', kwargs={'pk': self.kwargs['pk']})


class TodoListItemUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoListItem
    fields = ['title', 'text', 'done']
    context_object_name = 'todo_list_item'
    template_name = 'todo/list_item_update.html'

    def get_success_url(self):
        return reverse('todo:list-detail', kwargs={'pk': self.kwargs['id']})


class TodoListItemDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoListItem
    template_name = 'todo/list_item_delete.html'

    def get_success_url(self):
        return reverse('todo:list-detail', kwargs={'pk': self.kwargs['id']})
