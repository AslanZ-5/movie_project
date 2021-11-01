from django.shortcuts import render, redirect

from .models import Movie,Reviews
from django.views.generic import (
    ListView,
    DetailView,
)

from django.views.generic.base import View


class MoviesView(ListView):
    model = Movie
    template_name = 'main/movies.html'


# class MoviesView(View):
#
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'main/movies.html', {'movies': movies})


class MoviesDetailView(DetailView):
    model = Movie
    slug_field = 'url'


# class MoviesDetailView(View):
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, 'main/movie_detail.html', {'movie': movie})


class AddReview(View):
    def post(self, request, id):
        query = request.POST
        print(id)
        print(query)
        review = Reviews.objects.create(name=query['name'],email=query['email'],text=query['text'],movie_id=id)
        review.save()
        return redirect('/')
