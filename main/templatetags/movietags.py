from django import template
from main.models import CategoryModel

register = template.Library()

@register.simple_tag()
def get_categ():
    return CategoryModel.objects.all()