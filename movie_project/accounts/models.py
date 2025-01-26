from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# (Optimize) 별도 User 모델 확장
# (Clean) 필드 이름이 구체적이지 않을 수 있음 (ex: 'bio' 대신 'description', etc.)
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    # (Optimize) 추가로 사용될 Index
    class Meta:
        indexes = [
            models.Index(fields=['created_at']),
        ]

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=50, db_index=True)  # (Optimize) 검색 빈도 고려
    points = models.PositiveIntegerField(default=0)

    # (Clean) 단일 책임 분리 미흡: 현재 프로필만 다루지만,
    # 확장 시 CustomUser와 혼재될 가능성.
    def __str__(self):
        return f'{self.user.username} - {self.nickname}'
