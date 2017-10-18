from django.contrib import admin
from.models import TodoList, TodoListItem


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    date_hierarchy = 'created'
    ordering = ('-modified',)


@admin.register(TodoListItem)
class TodoListItemAdmin(admin.ModelAdmin):
    search_fields = ('title', )
    list_filter = ('done', )
