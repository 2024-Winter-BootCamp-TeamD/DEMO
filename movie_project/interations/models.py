from django.db import models
from django.conf import settings
from django.utils import timezone


class Lk(models.Model):
    usr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    ctype = models.CharField(max_length=50)
    oid = models.PositiveIntegerField()
    ctime = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return f"Lk by {self.usr} => {self.ctype}-{self.oid}"

class Bmk(models.Model):
    usr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_index=True)
    link = models.URLField()
    nt = models.CharField(max_length=100, blank=True)
    ctime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Bmk by {self.usr}: {self.link}"

class Fw(models.Model):
    fr = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fwg')
    to = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fwr')
    ctime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.fr} => {self.to}"
