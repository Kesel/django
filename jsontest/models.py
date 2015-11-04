from django.db import models


class Way(models.Model):
    steps = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
