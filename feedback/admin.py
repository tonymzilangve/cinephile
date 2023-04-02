from django.contrib import admin
from .models import *


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'critic', 'text', 'movie')
    list_display_links = ('id', 'critic', 'movie', )
    search_fields = ('critic', 'text', 'movie', )
    list_filter = ('critic', 'movie', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text')
    list_display_links = ('id', 'author', )
    search_fields = ('author',)
    list_filter = ('author', )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
