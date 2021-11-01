from django.shortcuts import render, redirect
from .forms import ReviewForm
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
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie_id = id
            form.save()

        # review = Reviews.objects.create(name=query['name'],email=query['email'],text=query['text'],movie_id=id)
        # review.save()
        return redirect('/')
