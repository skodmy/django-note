from django.conf.urls import url
from .views import TodoListListView, TodoListDetailView, TodoListItemDetailView

urlpatterns = [
    url(r'^todo_lists/', TodoListListView.as_view()),
    url(r'^todo_list/(?P<pk>\d+)/items/', TodoListDetailView.as_view()),
    url(r'^todo_list_item/(?P<pk>\d+)/', TodoListItemDetailView.as_view()),
]
