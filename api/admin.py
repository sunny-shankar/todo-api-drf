from django.contrib import admin
from api.models import TodoModel


@admin.register(TodoModel)
class TodoModelAdmin(admin.ModelAdmin):
    pass