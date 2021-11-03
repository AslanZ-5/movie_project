from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class PostAdminForm(forms.ModelForm):
    description = forms.CharField(label='Description', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


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

    def get_image(self, obj):
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
    actions = ['unpublish','publish']
    save_as = True
    form = PostAdminForm
    list_editable = ('draft',)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', ('poster', 'get_image'))
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

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.poster.url}" style="width:160px;height:150px;"')

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = '1 file has been updated'
        else:
            message_bit = f'{row_update} files has been updated'
        self.message_user(request, f'{message_bit}')

    get_image.short_description = 'Poster'

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = '1 file has been updated'
        else:
            message_bit = f'{row_update} files has been updated'
        self.message_user(request, f'{message_bit}')

    get_image.short_description = 'Poster'
    publish.short_description = 'To publish'
    unpublish.short_description = 'Un publish'
    publish.allowed_permissions = ('change',)


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
