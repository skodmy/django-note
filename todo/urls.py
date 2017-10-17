from django.conf.urls import url
from .views import TodoListListView, TodoListItemListView

urlpatterns = [
    url(r'^todo/todo_lists/', TodoListListView.as_view()),
    url(r'^todo/todo_list/items/', TodoListItemListView.as_view()),
]
