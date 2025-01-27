from django.db import models
from django.utils import timezone

class QueryLog(models.Model):
    # (Clean) 필드명 간략화, 주석 없음
    kw = models.CharField(max_length=100, db_index=True)
    ctime = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return f"{self.kw} at {self.ctime}"
