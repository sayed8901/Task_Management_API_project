from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):    
    list_display = ['id' ,'content', 'user', 'task', 'created_at',]


admin.site.register(Comment, CommentAdmin)
