from django.contrib import admin
from .models import *


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    list_display_links = ['id', 'name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url', 'draft']
    list_filter = ['category','year']
    search_fields = ('title','category__name')

admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(RatingStart)
admin.site.register(Reviews)
