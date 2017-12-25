from django.conf.urls import url, include
from .views import Index
from .views import TodoListCreateView, TodoListDetailView, TodoListUpdateView, TodoListDeleteView
from .views import TodoListItemCreateView, TodoListItemDetailView, TodoListItemUpdateView, TodoListItemDeleteView

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^list/', include([
        url('^add/$', TodoListCreateView.as_view(), name='list-add'),
        url(r'^(?P<todo_list_id>\d+)/', include([
            url(r'^$', TodoListDetailView.as_view(), name='list-detail'),
            url(r'^update/$', TodoListUpdateView.as_view(), name='list-update'),
            url(r'^delete/$', TodoListDeleteView.as_view(), name='list-delete'),
            url(r'^item/', include([
                url(r'add/$', TodoListItemCreateView.as_view(), name='list-item-add'),
                url(r'(?P<todo_list_item_id>\d+)/', include([
                    url(r'^$', TodoListItemDetailView.as_view(), name='list-item-detail'),
                    url(r'^update/$', TodoListItemUpdateView.as_view(), name='list-item-update'),
                    url(r'^delete/$', TodoListItemDeleteView.as_view(), name='list-item-delete'),
                ]))
            ]))
        ]))
    ])),
]
