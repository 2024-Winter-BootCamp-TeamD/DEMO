from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class usrModel(AbstractUser):
    bioinfo = models.TextField(blank=True)
    ctime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.username}"


class profOne(models.Model):
    usr = models.OneToOneField(usrModel, on_delete=models.CASCADE, related_name='prof')
    nick = models.CharField(max_length=50, db_index=True)
    pts = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.usr.username} => {self.nick}"
