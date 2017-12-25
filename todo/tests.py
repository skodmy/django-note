from django.test import TestCase, RequestFactory
from django.conf import settings
from django.apps import apps
from django.contrib.auth.models import AnonymousUser

from .models import TodoList, TodoListItem
from .views import Index
from .views import TodoListCreateView
from .views import TodoListItemCreateView, TodoListItemUpdateView, TodoListItemDeleteView


AUTH_USER_MODEL = apps.get_model(settings.AUTH_USER_MODEL)


class TodoListTestCase(TestCase):
    def setUp(self):
        self.todo_list = TodoList.objects.create(name='Test list', user=AUTH_USER_MODEL.objects.create())

    def test_datetime_logic(self):
        self.assertLessEqual(self.todo_list.created, self.todo_list.modified)

    def test_completed(self):
        self.assertTrue(self.todo_list.completed)


class TodoListItemTestCase(TestCase):
    def setUp(self):
        self.todo_list_item = TodoListItem.objects.create(
            title='Test item',
            todo_list=TodoList.objects.create(name='Test list', user=AUTH_USER_MODEL.objects.create()),
            text='Lorem ipsum dolor ... sit amet'
        )

    def test_done(self):
        self.assertFalse(self.todo_list_item.done)


class ViewTestCase(TestCase):
    def setUp(self):
        self._view = None
        self._request_factory = RequestFactory()
        self._user = AnonymousUser()


class ConcreteUserViewTestCase(ViewTestCase):
    def setUp(self):
        super().setUp()
        self._user = AUTH_USER_MODEL.objects.create()


class IndexViewTestCase(ConcreteUserViewTestCase):
    def setUp(self):
        super().setUp()
        self._view = Index()
        self._view.request = self._request_factory.get('/')
        self._view.request.user = self._user

    def test_get_queryset(self):
        for todo_list in self._view.get_queryset():
            self.assertEqual(todo_list.user, self._user)

    def test_as_view(self):
        response = Index.as_view()(self._view.request)
        self.assertEqual(response.status_code, 200)


class CRUDViewCommonMixinTestCase(TestCase):
    pass


class TodoListCRUDViewCommonMixinTestCase(TestCase):
    pass


class TodoListCreateViewTestCase(ConcreteUserViewTestCase):
    def setUp(self):
        super().setUp()
        self._view = TodoListCreateView()
        self._view.request = self._request_factory.get('/list/add/')
        self._view.request.user = self._user

    def test_form_valid(self):
        form = self._view.get_form_class()({'name': 'test_list'})
        self.assertEqual(self._view.form_valid(form).status_code, 302)

    def test_as_view(self):
        response = TodoListCreateView.as_view()(self._view.request)
        self.assertEqual(response.status_code, 200)


class TodoListDetailViewTestCase(TestCase):
    pass


class TodoListUpdateViewTestCase(TestCase):
    pass


class TodoListDeleteViewTestCase(TestCase):
    pass


class TodoListItemCRUDViewCommonMixinTestCase(TestCase):
    pass


class TodoListItemCreateViewTestCase(ConcreteUserViewTestCase):
    def setUp(self):
        super().setUp()
        self._view = TodoListItemCreateView()
        self._view.request = self._request_factory.get('/list/item/add/')
        self._view.request.user = self._user
        test_todo_list = TodoList.objects.create(name='test todo list', user=self._user)
        setattr(self._view, 'kwargs', {'todo_list_id': test_todo_list.id})

    def test_form_valid(self):
        form = self._view.get_form_class()({'title': 'test_list item', 'text': 'test_list item text'})
        self.assertEqual(self._view.form_valid(form).status_code, 302)

    def test_get_success_url(self):
        self.assertNotEqual(self._view.get_success_url(), '')

    def test_as_view(self):
        response = TodoListItemCreateView.as_view()(self._view.request)
        self.assertEqual(response.status_code, 200)


class TodoListItemDetailViewTestCase(ConcreteUserViewTestCase):
    pass


class TodoListItemUpdateViewTestCase(ConcreteUserViewTestCase):
    def setUp(self):
        super().setUp()
        self._view = TodoListItemUpdateView()
        test_todo_list = TodoList.objects.create(name='test todo list', user=self._user)
        setattr(self._view, 'kwargs', {'todo_list_id': test_todo_list.id})

    def test_get_success_url(self):
        self.assertNotEqual(self._view.get_success_url(), '')


class TodoListItemDeleteViewTestCase(ConcreteUserViewTestCase):
    def setUp(self):
        super().setUp()
        self._view = TodoListItemDeleteView()
        test_todo_list = TodoList.objects.create(name='test todo list', user=self._user)
        setattr(self._view, 'kwargs', {'todo_list_id': test_todo_list.id})

    def test_get_success_url(self):
        self.assertNotEqual(self._view.get_success_url(), '')
