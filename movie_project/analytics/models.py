from django.db import models
from django.utils import timezone

class AnalyticsRec(models.Model):
    # (Clean) 필드 이름들이 추상적이고, 주석 없음
    created = models.DateTimeField(default=timezone.now, db_index=True)
    dtype = models.CharField(max_length=50, db_index=True)
    val = models.IntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=['dtype', 'created']),
        ]

    def __str__(self):
        return f"{self.dtype} - {self.val} ({self.created.date()})"
