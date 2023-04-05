from django.contrib import admin
from .models import *


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_date', 'directors', 'budget', 'box_office', 'country')
    list_display_links = ('id', 'title', 'directors',)
    search_fields = ('title', 'genre', 'directors',)
    list_filter = ('title', 'genre', 'country',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    search_fields = ('name',)
    list_filter = ('name',)


class PrimaryCastAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'role', 'gender', 'birthday', 'citizenship', 'total_films')
    list_display_links = ('id', 'name', 'citizenship',)
    search_fields = ('name',)
    list_filter = ('role', 'gender', 'citizenship',)


class SecondaryCastAdmin(admin.ModelAdmin):
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


admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(PrimaryCast, PrimaryCastAdmin)
admin.site.register(SecondaryCast, SecondaryCastAdmin)

admin.site.register(MovieShot, MovieShotAdmin)
admin.site.register(Award, AwardAdmin)

admin.site.register(Critic, CriticAdmin)
