from django.conf.urls import url
from .views import TodoListListView, TodoListDetailView, TodoListItemDetailView

urlpatterns = [
    url(r'^lists/$', TodoListListView.as_view()),
    url(r'^list/(?P<pk>\d+)/$', TodoListDetailView.as_view()),
    url(r'^list-item/(?P<pk>\d+)/$', TodoListItemDetailView.as_view()),
]
