from django.db import models

class Bug(models.model):
    name = model.CharField(max_length=200)
    description = model.CharField(max_length=5000)
    status = models.IntegerField(default=0)
    project = models.ForeignKey('projects.Project')
    timestamp = models.DateTimeField('date published')