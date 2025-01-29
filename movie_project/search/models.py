from django.db import models
from django.utils import timezone


class SQ(models.Model):
    ky = models.CharField(max_length=100, db_index=True)
    ct = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return f"{self.ky} / {self.ct}"
