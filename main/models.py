import datetime

from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.SlugField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    name = models.CharField(max_length=255)
    age = models.SmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actor and director'
        verbose_name_plural = 'Actors and directors'


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    url = models.SlugField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    title = models.CharField(max_length=255)
    tagline = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='movies/')
    year = models.PositiveSmallIntegerField('date of release',default=2010)
    country = models.CharField(max_length=150)
    directors = models.ManyToManyField(Actor, verbose_name='directors', related_name='film_directors')
    actors = models.ManyToManyField(Actor,verbose_name='actors',related_name='film_actors')
    genres = models.ManyToManyField(Genre)
    world_premiere = models.DateField(default=datetime.date.today)
    budget = models.PositiveSmallIntegerField(default=0, help_text='specify amount in dollars')
    fees_in_usa = models.PositiveSmallIntegerField(default=0,help_text='specify amount in dollars')
    fees_in_world = models.PositiveSmallIntegerField(default=0,help_text='specify amount in dollars')
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160,unique=True)
    