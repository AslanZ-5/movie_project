from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Movie
from .serializers import MovieListSerializer,MovieDetailSerializer,ReviewCreateSerializer


class MovieApiListView(APIView):

    def get(self, request):
        movies = Movie.objects.filter(draft=False)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


class MovieApiDetailView(APIView):

    def get(self, request,pk):
        movies = Movie.objects.get(id=pk,draft=False)
        serializer = MovieDetailSerializer(movies)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    def post(self,request):
        review = ReviewCreateSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response(status=201)
