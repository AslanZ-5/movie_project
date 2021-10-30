from django.urls import path,include
from .views import MoviesView,MoviesDetailView

urlpatterns = [
    path('',MoviesView.as_view(),name='movies'),
    path('detail/<int:pk>/',MoviesDetailView.as_view(),name='movie_detail')
]