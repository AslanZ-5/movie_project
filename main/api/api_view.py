from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from main.models import Movie, Actor
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer, CreateRatingSerializer, \
    ActorListSerializer, ActorDetailSerializer
from .service import get_client_ip, MovieFilter, LargeResultsSetPagination
from django.db.models import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet, ModelViewSet


class MovieViewSet(ReadOnlyModelViewSet):
    pagination_class = LargeResultsSetPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter

    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=Count('ratings', filter=Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            # middle_star=Sum(F('ratings__star'))/ Count(F('ratings'))
            middle_star=Avg('ratings__star')
        )
        return movies

    def get_serializer_class(self):
        if self.action == 'list':
            return MovieListSerializer
        elif self.action == 'retrieve':
            return MovieDetailSerializer


# class MovieApiListView(ListAPIView):
#     serializer_class = MovieListSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = MovieFilter
#     # permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         movies = Movie.objects.filter(draft=False).annotate(
#             rating_user=Count('ratings', filter=Q(ratings__ip=get_client_ip(self.request)))
#         ).annotate(
#             # middle_star=Sum(F('ratings__star'))/ Count(F('ratings'))
#             middle_star=Avg('ratings__star')
#         )
#         return movies


# class MovieApiDetailView(RetrieveAPIView):
#     queryset = Movie.objects.filter(draft=False)
#     serializer_class = MovieDetailSerializer
#

#
# class ReviewCreateView(APIView):
#     def post(self, request):
#         review = ReviewCreateSerializer(data=request.data)
#         if review.is_valid():
#             review.save()
#         return Response(status=201)

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewCreateSerializer


# class ReviewCreateView(CreateAPIView):
#     serializer_class = ReviewCreateSerializer


# class AddStarRatingView(APIView):
#
#     def post(self, request):
#         serializer = CreateRatingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(ip=get_client_ip(request))
#             return Response(status=201)
#         else:
#             return Response(status=400)


class AddStarViewSet(ModelViewSet):
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


# class AddStarRatingView(CreateAPIView):
#     serializer_class = CreateRatingSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(ip=get_client_ip(self.request))


class ActorViewSet(ViewSet):
    def list(self, request):
        queryset = Actor.objects.all()
        serializer = ActorListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Actor.objects.all()
        actor = get_object_or_404(queryset, pk=pk)
        serializer = ActorDetailSerializer(actor)
        return Response(serializer.data)

# class ActorAPIListView(ListAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorListSerializer
#
#
# class ActorAPIDetailView(RetrieveAPIView):
#     queryset = Actor.objects.all()
#     serializer_class = ActorDetailSerializer
