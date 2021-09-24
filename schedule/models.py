from django.db import models

class Assignment(models.Model):
    course = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    due_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
