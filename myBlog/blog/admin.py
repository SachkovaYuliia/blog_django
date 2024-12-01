from django.contrib import admin
from .models import Post, Category, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('author', 'date')
    search_fields = ('title', 'description')

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
