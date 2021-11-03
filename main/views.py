from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Movie, Reviews, CategoryModel, Actor
from django.views.generic import (
    ListView,
    DetailView,
)

from django.views.generic.base import View


class MoviesView(ListView):
    model = Movie
    template_name = 'main/movies.html'
    queryset = Movie.objects.filter(draft=False)


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
        movie = Movie.objects.get(id=id)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie_id = id
            form.save()

        # review = Reviews.objects.create(name=query['name'],email=query['email'],text=query['text'],movie_id=id)
        # review.save()
        return redirect(movie.get_absolute_url())


class ActorsView(ListView):
    model = Actor
    template_name = 'main/actors.html'


class ActorDetailView(DetailView):
    model = Actor
    slug_field = 'name'


    def get_object(self, queryset=None):

        if queryset is None:
            queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        unslug = slug.replace('-', ' ')
        if slug:
            queryset = queryset.filter(**{self.slug_field: unslug})

        return queryset.get()
