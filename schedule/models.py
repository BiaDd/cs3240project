import datetime
from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib import admin


class Assignment(models.Model):
    course = models.CharField(max_length=200, default="class")
    title = models.CharField(max_length=200, default="assignment name")
    description = models.CharField(max_length=200, default="description")
    date_created = models.DateTimeField('date created')
    due_date = models.DateTimeField('due date')

    def __str__(self):
        return self.title