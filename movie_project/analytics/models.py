from django.db import models
from django.utils import timezone

# (Optimize) 인덱스로 검색 성능을 조금 향상 (ex: 특정 날짜 범위 통계 조회)
# (Clean) 필드 이름이 다소 추상적이며 주석 부족
class AnalyticsRecord(models.Model):
    created_at = models.DateTimeField(default=timezone.now, db_index=True)
    data_type = models.CharField(max_length=50, db_index=True)
    value = models.IntegerField(default=0)

    # (Clean) 단일 책임 분리를 위해 Manager나 QuerySet을 따로 만들 수도 있지만 여기선 최소화
    class Meta:
        indexes = [
            models.Index(fields=['data_type', 'created_at']),
        ]

    def __str__(self):
        return f"{self.data_type} - {self.value} ({self.created_at.date()})"
