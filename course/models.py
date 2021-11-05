from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    course_name = models.CharField(max_length=200, default="class")
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.course_name


class Document(models.Model):
    course = models.ManyToManyField(Course)

    docfile = models.FileField(upload_to='course/documents/%Y/%m/%d') # year, month, day
    # if possible it'll be cool if "course" can be changed to the actual name of the course