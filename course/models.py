from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_out
from django.contrib import messages


class Course(models.Model):
    course_name = models.CharField(max_length=200, default="class")
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.course_name

class Document(models.Model):
    course = models.ManyToManyField(Course)

    docfile = models.FileField(upload_to='course/documents/%Y/%m/%d') # year, month, day
    # if possible it'll be cool if "course" can be changed to the actual name of the course

# when a user logs out, display a confirmation message
def logout_task(sender, user, request, **kwargs):
    messages.add_message(
        request,
        messages.INFO,
        f"You are successfully logged out.",
    )
user_logged_out.connect(logout_task)
