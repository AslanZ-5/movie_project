from django.contrib import admin
from .models import *

admin.site.register(CategoryModel)
admin.site.register(Movie)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(RatingStart)
admin.site.register(Reviews)

