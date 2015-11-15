from django.db import models


class Way(models.Model):
    steps = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)


class DailySteps(models.Model):
    day = models.CharField(max_length=8)
    steps = models.IntegerField(default=0)
