from django.db import models

class Schedule(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Event(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    when = models.DateTimeField(blank=False, null=False)  # Не допускаем пустые значения
    where = models.CharField(max_length=200)
    who = models.CharField(max_length=200)