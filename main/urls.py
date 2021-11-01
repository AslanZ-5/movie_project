from django.urls import path,include
from .views import MoviesView,MoviesDetailView,AddReview

urlpatterns = [
    path('',MoviesView.as_view(),name='movies'),
    path('detail/<str:slug>/',MoviesDetailView.as_view(),name='movie_detail'),
    path('<int:id>/',AddReview.as_view(),name='add_review')
]