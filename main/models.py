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


