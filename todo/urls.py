from django.conf.urls import url
from .views import TodoListListView, TodoListItemListView

urlpatterns = [
    url(r'^todo_lists/', TodoListListView.as_view()),
    url(r'^todo_list/(?P<todo_list_id>\d+)/items/', TodoListItemListView.as_view()),
]
