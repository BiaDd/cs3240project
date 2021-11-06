from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_out
from django.contrib import messages
import os


class Course(models.Model):
    course_name = models.CharField(max_length=200, default="class")
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.course_name

class Document(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    docfile = models.FileField(upload_to='course/documents/%Y/%m/%d') # year, month, day

    def filename(self): # remove a full path from the filename
        return os.path.basename(self.docfile.name)
    def __str__(self): # use the formatted pathname for its string representation
        return self.filename()

# when a user logs out, display a confirmation message
def logout_task(sender, user, request, **kwargs):
    messages.add_message(
        request,
        messages.INFO,
        f"You are successfully logged out.",
    )
user_logged_out.connect(logout_task)
