from django.urls import path,include
from .views import MoviesView

urlpatterns = [
    path('',MoviesView.as_view(),name='movies'),
]