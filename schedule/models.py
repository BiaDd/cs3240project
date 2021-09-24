# from django.db import models

# class Assignment(models.Model):
    # course = models.CharField(max_length=200)
    # title = models.CharField(max_length=200)
    # description = models.CharField(max_length=200)
    # due_date = models.DateTimeField('date published')
    # def __str__(self):
        # return self.title

import datetime
from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib import admin




# Create your models here.
class Assignment(models.Model):
    def __str__(self):
        return self.assignment_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


    title = models.CharField(max_length=200, default="title")
    assignment_text = models.CharField(max_length=2000, default="type here")
    pub_date = models.DateTimeField('date published')
