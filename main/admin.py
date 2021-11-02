from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url']
    list_display_links = ['id', 'name']


class ReviewLine(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ['name']


class ShotsLine(admin.StackedInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self,obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:260px;height:200px;"')

    get_image.short_description = 'Image'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url', 'draft']
    list_filter = ['category', 'year']
    readonly_fields = ('get_image',)
    search_fields = ('title', 'category__name')
    inlines = [ReviewLine, ShotsLine]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', ('poster','get_image'))
        }),
        (None, {
            'fields': (('year', 'country', 'world_premiere'),)
        }),

        (None, {
            'fields': (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ('url and draft', {
            'classes': ('collapse',),
            'fields': (('url', 'draft'),)
        })

    )
    def get_image(self,obj):
        return mark_safe(f'<img src="{obj.poster.url}" style="width:160px;height:150px;"')

    get_image.short_description = 'Poster'



@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'parent', 'movie']
    readonly_fields = ['name', 'email']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'get_image']
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:40px;height:40px;"')

    get_image.short_description = 'Image'


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ['title', 'movie']
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width:260px;height:200px;"')

    get_image.short_description = 'Image'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['ip', 'star', 'movie']


@admin.register(RatingStart)
class RatingStartAdmin(admin.ModelAdmin):
    list_display = ['value']


admin.site.site_title = 'dj'
admin.site.site_header = 'dj site'
