from django.db import models
from django.utils.timezone import now
from accounts.models import Profile
from projects.models import Project


class Feature(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    status = models.CharField(default='To Do', max_length=20)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    timestamp = models.DateTimeField('date published', default=now, blank=True)
    upvotes = models.IntegerField(default=0)

    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def is_active(self):
        return self.status
