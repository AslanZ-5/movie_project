from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Movie, Reviews, CategoryModel
from django.views.generic import (
    ListView,
    DetailView,
)

from django.views.generic.base import View


class MoviesView(ListView):
    model = Movie
    template_name = 'main/movies.html'
    queryset = Movie.objects.filter(draft=False)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        return context


# class MoviesView(View):
#
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'main/movies.html', {'movies': movies})


class MoviesDetailView(DetailView):
    model = Movie
    slug_field = 'url'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        return context



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
