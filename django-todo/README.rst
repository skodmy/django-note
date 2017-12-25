=====
Todo
=====

Todo is a simple Django app to conduct Web-based todo lists.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "todo" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'todo',
    ]

2. Include the todo URLconf in your project urls.py like this::

    url(r'^todo/', include(todo.urls, namespace='todo')),

3. Run `python manage.py migrate` to create the todo models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/todo/ to participate in the todo.
