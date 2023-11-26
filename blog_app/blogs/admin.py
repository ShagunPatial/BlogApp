from django.contrib import admin
from .models import Blog, Comment, Reaction

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')  # Enables searching by title and author's username

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'blog', 'created_at')
    search_fields = ('content', 'author__username')  # Enables searching by content and author's username

@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'reaction_type', 'created_at', 'blog_post', 'comment')
    search_fields = ('user__username',)  # Enables searching by user's username
