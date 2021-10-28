from django.db import models
from django.utils import timezone

# user model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# model for the user
# https://www.youtube.com/watch?v=c-SVweZiiKs
# https://docs.djangoproject.com/en/3.2/topics/db/examples/one_to_one/

class Student(models.Model):
    '''
    Student profile
    '''
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    ) # links user with info

    existing_user = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username


# model that holds data for an assignment
class Assignment(models.Model):
    """
    This model is user specific (each user has their own assignments)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #primary key?
    course = models.CharField(max_length=200, default="class")
    title = models.CharField(max_length=200, default="assignment name")
    description = models.CharField(max_length=200, default="description")
    date_created = models.DateTimeField('date created', default=timezone.now())
    due_date = models.DateTimeField('due date', default=timezone.now())

    def __str__(self):
        return self.title


@receiver(post_save, sender=User, dispath_uid="create_user")
def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User, dispatch_uid="link_user_to_student")
def user_to_student(sender, instance, **kwargs):
    instance.student.save()