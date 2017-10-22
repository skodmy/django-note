from django.conf.urls import url
from .views import TodoListDetailView, TodoListItemDetailView, Index, TodoListCreateView, \
    TodoListUpdateView, TodoListDeleteView, TodoListItemCreateView, TodoListItemUpdateView, TodoListItemDeleteView

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^list/add/$', TodoListCreateView.as_view(), name='list-add'),
    url(r'^list/(?P<pk>\d+)/update/$', TodoListUpdateView.as_view(), name='list-update'),
    url(r'^list/(?P<pk>\d+)/delete/$', TodoListDeleteView.as_view(), name='list-delete'),
    url(r'^list/(?P<pk>\d+)/$', TodoListDetailView.as_view(), name='list-detail'),
    url(r'^list/(?P<id>\d+)/list-item/(?P<pk>\d+)/$', TodoListItemDetailView.as_view(), name='list-item-detail'),
    url(r'^list/(?P<pk>\d+)/list-item/add/$', TodoListItemCreateView.as_view(), name='list-item-add'),
    url(r'^list/(?P<id>\d+)/list-item/(?P<pk>\d+)/update/$', TodoListItemUpdateView.as_view(), name='list-item-update'),
    url(r'^list/(?P<id>\d+)/list-item/(?P<pk>\d+)/delete/$', TodoListItemDeleteView.as_view(), name='list-item-delete')
]
