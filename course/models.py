from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name = models.CharField(max_length=200, default="class")
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.course_name
