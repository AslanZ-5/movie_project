import datetime

from django.db import models
from django.urls import reverse


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
    tagline = models.CharField(max_length=100, default='')
    description = models.TextField()
    poster = models.ImageField(upload_to='movies/')
    year = models.PositiveSmallIntegerField('date of release', default=2010)
    country = models.CharField(max_length=150)
    directors = models.ManyToManyField(Actor, verbose_name='directors', related_name='film_directors')
    actors = models.ManyToManyField(Actor, verbose_name='actors', related_name='film_actors')
    genres = models.ManyToManyField(Genre)
    world_premiere = models.DateField(default=datetime.date.today)
    budget = models.PositiveSmallIntegerField(default=0, help_text='specify amount in dollars')
    fees_in_usa = models.PositiveSmallIntegerField(default=0, help_text='specify amount in dollars')
    fees_in_world = models.PositiveSmallIntegerField(default=0, help_text='specify amount in dollars')
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    def review_get(self):
        return self.reviews_set.filter(parent=None)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class MovieShots(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='movie_shots/')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Shot from Movie'
        verbose_name_plural = 'Shots from Movie'


class RatingStart(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value


class Rating(models.Model):
    ip = models.CharField('ip address', max_length=15)
    star = models.ForeignKey(RatingStart, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star}  {self.movie}'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'
