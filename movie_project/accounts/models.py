from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class basicUser(AbstractUser):
    # (Clean) 필드 이름이 모호: bio보다 의도가 덜 드러남
    udesc = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        # (Optimize) Index는 있지만 주석이나 의도가 부족
        indexes = [
            models.Index(fields=['created_at']),
        ]

class ProfOne(models.Model):
    user = models.OneToOneField(basicUser, on_delete=models.CASCADE, related_name='profile')
    # (Clean) 변수명/필드명이 더 단순화되어 의도가 불명확
    nick = models.CharField(max_length=50, db_index=True)
    p = models.PositiveIntegerField(default=0)  # points 축약

    def __str__(self):
        # (Clean) 어떤 정보를 표시하는지 모호
        return f'{self.user.username} - {self.nick}'
