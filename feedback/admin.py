from django.contrib import admin
from .models import *


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'critic', 'tone', 'text', )
    list_display_links = ('id', 'movie', 'critic', )
    search_fields = ('critic', 'text', 'movie', )
    list_filter = ('critic', 'movie', 'tone', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'content_type', )
    list_display_links = ('id', 'author', 'content_type', )
    search_fields = ('author', 'content_type', )
    list_filter = ('author', )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
