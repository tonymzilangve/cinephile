from django.contrib import admin
from .models import *


class MovieAadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'genre', 'release_date', 'director', 'budget', 'box_office', 'country')
    list_display_links = ('id', 'name', 'director',)
    search_fields = ('name', 'genre', 'director',)
    list_filter = ('name', 'genre', 'director', 'country',)


class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'birthday', 'citizenship', 'film_count')
    list_display_links = ('id','name', 'citizenship',)
    search_fields = ('name',)
    list_filter = ('name', 'gender', 'citizenship',)


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_filter = ('name',)


class OperatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_filter = ('name',)


class ScriptWriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_filter = ('name',)


class ComposerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_filter = ('name',)


class MovieShotAdmin(admin.ModelAdmin):
    list_display = ('id', 'desc', 'movie')
    list_display_links = ('id', 'movie',)
    search_fields = ('movie',)
    list_filter = ('movie',)


class AwardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_filter = ('name',)


class CriticAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_filter = ('name',)


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


admin.site.register(Movie, MovieAadmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(ScriptWriter, ScriptWriterAdmin)
admin.site.register(Composer, ComposerAdmin)
admin.site.register(MovieShot, MovieShotAdmin)
admin.site.register(Award, AwardAdmin)
admin.site.register(Critic, CriticAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
