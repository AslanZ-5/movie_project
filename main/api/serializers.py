from rest_framework import serializers
from main.models import Movie, Reviews



class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','title', 'tagline', 'category', 'actors')


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('name','text','parent')


class MovieDetailSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name_en', read_only=True)
    directors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field='name_en', read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name_en', read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        # exclude = ('draft',)
        fields = ('title', 'tagline', 'description', 'poster', 'year'
                  , 'country', 'world_premiere', 'budget', 'fees_in_usa',
                  'fees_in_world', 'category', 'directors', 'actors',
                  'genres', 'reviews'
                  )
