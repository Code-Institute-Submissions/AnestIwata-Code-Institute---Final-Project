from django.db import models

class Feature(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    status = models.IntegerField(default=0)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    timestamp = models.DateTimeField('date published')
    upvotes = models.IntegerField(default=0)
    # author = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def is_active(self):
        return self.status