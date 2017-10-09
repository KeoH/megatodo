from django.contrib import admin

from .models import Todo, Task, Comment


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author','create_date']

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'create_date']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'todo']

admin.site.register(Todo, TodoAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(Comment, CommentAdmin)