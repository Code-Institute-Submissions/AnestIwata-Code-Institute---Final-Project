from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    status = models.IntegerField(default=0)
    timestamp = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    def is_active(self):
        return self.status
