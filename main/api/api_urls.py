from django.urls import path
from . import api_view

urlpatterns = [
    path('api-movie/', api_view.MovieViewSet.as_view({'get': 'list'})),
    path('api-movie/<int:pk>/', api_view.MovieViewSet.as_view({'get': 'retrieve'})),
    path('review/', api_view.ReviewViewSet.as_view({'post': 'create'})),
    path('rating/', api_view.AddStarViewSet.as_view({'post': 'create'})),
    path('actors/', api_view.ActorViewSet.as_view({'get': 'list'})),
    path('actor/<int:pk>/', api_view.ActorViewSet.as_view({'get': 'retrieve'})),
]
