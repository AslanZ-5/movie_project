from django.urls import path
from . import api_view

urlpatterns = [
    path('api-movie/', api_view.MovieApiListView.as_view()),
    path('api-movie/<int:pk>/', api_view.MovieApiDetailView.as_view()),
    path('review/', api_view.ReviewCreateView.as_view()),
]