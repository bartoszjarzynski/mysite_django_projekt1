from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)
    actions = ['delete_selected']
    ordering = ('-created_at',)
    list_per_page = 20

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'text', 'created_at')
    search_fields = ('name', 'email', 'text')
    list_filter = ('created_at',)
    actions = ['delete_selected']
    ordering = ('-created_at',)
    list_per_page = 20
