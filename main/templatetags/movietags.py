from django import template
from main.models import CategoryModel, Movie

register = template.Library()


@register.simple_tag()
def get_categ():
    return CategoryModel.objects.all()


@register.inclusion_tag('main/last_added.html')
def get_last_movie(count = 5):
    movies = Movie.objects.order_by('id')[:count]
    return {'last_movies': movies}
