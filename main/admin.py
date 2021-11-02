from django.contrib import admin
from .models import *


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    list_display_links = ['id', 'name']


class ReviewLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ['name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url', 'draft']
    list_filter = ['category', 'year']
    search_fields = ('title', 'category__name')
    inlines = [ReviewLine]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description','poster')
        }),
        (None, {
            'fields': (('year', 'country','world_premiere'),)
        }),

        (None, {
            'fields': (('actors', 'directors','genres','category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ('url and draft', {
            'classes':('collapse',),
            'fields': (('url','draft'),)
        })

    )


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'parent', 'movie']
    readonly_fields = ['name', 'email']




admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(RatingStart)
