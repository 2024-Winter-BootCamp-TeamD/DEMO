from rest_framework import serializers
from .models import Movie, Review

class MovieDataSerializer(serializers.ModelSerializer):
    # (Clean 측면) 필드 커스텀 최소화, 이름이 다소 애매모호
    review_items = serializers.StringRelatedField(many=True, source='reviews')

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'released_at', 'review_items']


class ReviewDataSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(source='movie.title', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'content', 'score', 'created_at', 'movie_title']