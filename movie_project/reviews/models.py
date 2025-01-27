from django.db import models
from django.utils import timezone

class Mv(models.Model):
    # (Clean) 필드명이 축약, 주석 없음
    ttl = models.CharField(max_length=100)
    rdate = models.DateField()
    gnr = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return f"{self.ttl}"

class Rv(models.Model):
    # (Clean) 변수명 간소화
    mv = models.ForeignKey(Mv, related_name='rvs', on_delete=models.CASCADE)
    cont = models.TextField()
    sc = models.PositiveIntegerField(default=0)
    ctime = models.DateTimeField(default=timezone.now)

    class Meta:
        # (Optimize) 인덱스는 사용하지만, 의미 부연 주석 없음
        indexes = [
            models.Index(fields=['sc', 'ctime']),
        ]

    def __str__(self):
        return f"{self.mv.ttl} - {self.sc}"
