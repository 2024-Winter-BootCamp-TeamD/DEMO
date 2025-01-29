from django.db import models
from django.utils import timezone


class Mv(models.Model):
    ttl = models.CharField(max_length=100)
    rdate = models.DateField()
    gnr = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return f"{self.ttl}"

class Rv(models.Model):
    mv = models.ForeignKey(Mv, related_name='rvs', on_delete=models.CASCADE)
    cont = models.TextField()
    sc = models.PositiveIntegerField(default=0)
    ctime = models.DateTimeField(default=timezone.now)

    class Meta:
        indexes = [
            models.Index(fields=['sc', 'ctime']),
        ]

    def __str__(self):
        return f"{self.mv.ttl} - {self.sc}"
