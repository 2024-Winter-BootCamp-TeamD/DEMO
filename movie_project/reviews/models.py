from django.db import models
from django.utils import timezone

class Movie(models.Model):
    # (Clean) 필드명은 비교적 간단하지만 주석이나 세부 설명 부족
    title = models.CharField(max_length=100)
    released_at = models.DateField()
    genre = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField()
    score = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        indexes = [
            models.Index(fields=['score', 'created_at']),
        ]

    def __str__(self):
        return f"{self.movie.title} - {self.score}"
