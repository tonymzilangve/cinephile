from django.contrib import admin
from .models import *


class MovieAadmin:
    pass


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'critic', 'text')
    list_display_links = ('id', 'critic', )
    search_fields = ('critic',)
    list_filter = ('critic', )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text')
    list_display_links = ('id', 'author', )
    search_fields = ('author',)
    list_filter = ('author', )


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)