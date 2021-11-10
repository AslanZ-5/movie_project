from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Movie, Actor
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer, CreateRatingSerializer, \
    ActorListSerializer, ActorDetailSerializer
from .service import get_client_ip
from django.db.models import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView


class MovieApiListView(ListAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=Count('ratings', filter=Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            # middle_star=Sum(F('ratings__star'))/ Count(F('ratings'))
            middle_star=Avg('ratings__star')
        )
        return movies


class MovieApiDetailView(RetrieveAPIView):
    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieDetailSerializer


#
# class ReviewCreateView(APIView):
#     def post(self, request):
#         review = ReviewCreateSerializer(data=request.data)
#         if review.is_valid():
#             review.save()
#         return Response(status=201)

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewCreateSerializer


# class AddStarRatingView(APIView):
#
#     def post(self, request):
#         serializer = CreateRatingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(ip=get_client_ip(request))
#             return Response(status=201)
#         else:
#             return Response(status=400)


class AddStarRatingView(CreateAPIView):
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class ActorAPIListView(ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorAPIDetailView(RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer
