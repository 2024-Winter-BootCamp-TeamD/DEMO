from django.db import models
from django.utils import timezone

class Movie(models.Model):
    title = models.CharField(max_length=100)
    released_at = models.DateField()
    # (Optimize 측면) DB 인덱스 생성으로 검색 성능 향상
    # (Clean 측면) index 속성 사용은 좋지만, Meta에 별도로 기술하거나
    # 필드명을 더 명확하게 하지 않아도 된다는 점은 다소 애매함
    genre = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    score = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    # (Optimize 측면) 특정 질의에 사용될 수 있는 인덱스
    class Meta:
        indexes = [
            models.Index(fields=['score', 'created_at']),
        ]

    def __str__(self):
        return f"{self.movie.title} - {self.score}"