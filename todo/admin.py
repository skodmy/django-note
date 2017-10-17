from django.contrib import admin
from.models import TodoList, TodoListItem


class TodoAdmin(admin.ModelAdmin):
    """
    Admin class for abstract Todo model.
    """
    date_hierarchy = 'created_at'
    ordering = ('-last_modified_at', )
    search_fields = ('name', )


@admin.register(TodoList)
class TodoListAdmin(TodoAdmin):
    pass


@admin.register(TodoListItem)
class TodoListItemAdmin(TodoAdmin):
    list_filter = ('checked', )
