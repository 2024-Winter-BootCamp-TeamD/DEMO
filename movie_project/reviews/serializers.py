from rest_framework import serializers
from .models import Movie, Review

class movieData(serializers.ModelSerializer):
    # (Clean) 변수명 review_items가 의도가 분명치 않음
    review_items = serializers.StringRelatedField(many=True, source='reviews')

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'released_at', 'review_items']

class revData(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'content', 'score', 'created_at', 'movie_title']
