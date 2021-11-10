from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer, ReviewCreateSerializer, CreateRatingSerializer
from .service import get_client_ip
from django.db.models import Case,When,BooleanField


class MovieApiListView(APIView):

    def get(self, request):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user = Case(When(ratings__ip=get_client_ip(request),then=True),
                               default=False,
                               output_field=BooleanField()),
        )
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieApiDetailView(APIView):

    def get(self, request, pk):
        movies = Movie.objects.get(id=pk, draft=False)
        serializer = MovieDetailSerializer(movies)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    def post(self, request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)


class AddStarRatingView(APIView):

    def post(self, request):
        serializer = CreateRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)
