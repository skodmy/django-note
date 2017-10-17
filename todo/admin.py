from django.contrib import admin
from.models import Todo, TodoList, TodoListItem


class TodoAdmin(admin.ModelAdmin):
    """
    Admin class for Todo.
    """
    date_hierarchy = 'created_at'
    ordering = '-last_modified_at'
    search_fields = ('name', )


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    pass


@admin.register(TodoListItem)
class TodoListItemAdmin(admin.ModelAdmin):
    list_filter = ('checked', admin.BooleanFieldListFilter)
