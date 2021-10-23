from django.db import models
from django.db import models
from django.utils import timezone

class Assignment(models.Model):
    course = models.CharField(max_length=200, default="class")
    title = models.CharField(max_length=200, default="assignment name")
    description = models.CharField(max_length=200, default="description")
    date_created = models.DateTimeField('date created', default=timezone.now())
    due_date = models.DateTimeField('due date', default=timezone.now())

    def __str__(self):
        return self.title
