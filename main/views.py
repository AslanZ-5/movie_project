from django.shortcuts import render
from .models import Movie
from django.views.generic.base import View


class MoviesView(View):

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'main/movies.html', {'movies': movies})


class MoviesDetailView(View):
    def get(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        return render(request, 'main/movie_detail.html', {'movie': movie})
