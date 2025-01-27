from django.db import models
from django.utils import timezone

class SQ(models.Model):
    # (Clean) 변수명 축약, 주석 없음
    ky = models.CharField(max_length=100, db_index=True)
    ct = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        # (Clean) 모호한 리턴 형식
        return f"{self.ky} / {self.ct}"
