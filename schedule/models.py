from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # instead of User, Student later?
    course = models.CharField(max_length=200, default="class")
    title = models.CharField(max_length=200, default="assignment name")
    description = models.CharField(max_length=200, default="description")
    date_created = models.DateTimeField('date created', default=timezone.now)
    due_date = models.DateTimeField('due date', default=timezone.now)

    def __str__(self):
        return self.title
