from django.db import models

class Assignment(models.Model):
    course = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField('date created')
    due_date = models.DateTimeField('due date')

    def __str__(self):
        return self.title
