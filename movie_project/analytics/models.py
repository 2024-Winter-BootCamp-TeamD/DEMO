from django.db import models
from django.utils import timezone


class ARec(models.Model):
    dt = models.CharField(max_length=50, db_index=True)
    val = models.IntegerField(default=0)
    ctime = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return f"{self.dt}-{self.val}"
