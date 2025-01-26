from django.db import models
from django.utils import timezone

# (Optimize) 인덱스를 사용해 검색 로그 조회를 빠르게 할 수 있음
# (Clean) 모델 구조가 간단하지만, 주석 부족
class SearchQuery(models.Model):
    keyword = models.CharField(max_length=100, db_index=True)
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return f"{self.keyword} at {self.created_at}"
