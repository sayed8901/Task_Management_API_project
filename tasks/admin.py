from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):    
    list_display = ['id' ,'title', 'description', 'status', 'priority', 'assigned_to', 'project', 'created_at', 'due_date']


admin.site.register(Task, TaskAdmin)
