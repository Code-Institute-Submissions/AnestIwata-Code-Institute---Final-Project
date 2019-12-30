from django.db import models

class Project(models.model):
    name = model.CharField(max_length=200)
    description = model.CharField(max_length=5000)
    status = models.IntegerField(default=0)
    timestamp = models.DateTimeField('date published')