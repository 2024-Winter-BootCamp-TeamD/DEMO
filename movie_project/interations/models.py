from django.db import models
from django.conf import settings
from django.utils import timezone

# (Optimize) 인덱스 활용, ForeignKey select_related 가능
# (Clean) 모델 이름은 직관적이지만 주석이나 추가 책임 분리가 부족
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    content_type = models.CharField(max_length=50)  # (Clean) 어떤 모델을 Like하는지 모호
    object_id = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['content_type', 'object_id']),
        ]

    def __str__(self):
        return f"Like by {self.user} on {self.content_type}-{self.object_id}"

class Bookmark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    url = models.URLField()
    note = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Bookmark by {self.user}: {self.url}"

class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.follower} follows {self.following}"
