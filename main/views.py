from django.shortcuts import render, redirect
from .forms import ReviewForm, RatingForm
from .models import Movie, Reviews, CategoryModel, Actor, Genre, Rating, RatingStart
from django.views.generic import (
    ListView,
    DetailView,
)
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic.base import View


# This class has data getting methods
# after inheriting to View class we'll get access
# to the methods in html with context data "view"
# example: view.get_genres
class GenreYear:
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')


class MoviesView(GenreYear, ListView):
    model = Movie
    paginate_by = 2
    template_name = 'main/movies.html'
    queryset = Movie.objects.filter(draft=False)


# class MoviesView(View):
#
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'main/movies.html', {'movies': movies})


class MoviesDetailView(GenreYear, DetailView):
    model = Movie
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['star_form'] = RatingForm()
        return context


# class MoviesDetailView(View):
#     def get(self, request, slug):
#         movie = Movie.objects.get(url=slug)
#         return render(request, 'main/movie_detail.html', {'movie': movie})


class AddReview(GenreYear, View):
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


class ActorsView(GenreYear, ListView):
    model = Actor
    template_name = 'main/actors.html'


class ActorDetailView(GenreYear, DetailView):
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


class FilterMoviesView(GenreYear, ListView):
    template_name = 'main/movies.html'
    paginate_by = 2

    def get_queryset(self):
        queryset = Movie.objects.filter(Q(year__in=self.request.GET.getlist('year')) |
                                        Q(genres__in=self.request.GET.getlist('genre'))).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['year'] = ''.join([f'year={x}&' for x in self.request.GET.getlist('year')])
        context['genre'] = ''.join([f'genre={x}&' for x in self.request.GET.getlist('genre')])
        return context


class AddRatingView(View):
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        form = RatingForm(request.POST)
        if form.is_valid():
            Rating.objects.update_or_create(
                ip=self.get_client_ip(request),
                movie_id=int(request.POST.get("movie")),
                defaults={'star_id': int(request.POST.get('star'))}
            )
            return HttpResponseRedirect('/')
        else:
            return HttpResponse(status=400)


class SearchMovie(ListView):
    template_name = 'main/movies.html'
    paginate_by = 2

    def get_queryset(self):
        queryset = Movie.objects.filter(title__icontains=self.request.GET.get('q'))
        return queryset

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['q'] = f'q={self.request.GET.get("q")}&'
        return context
