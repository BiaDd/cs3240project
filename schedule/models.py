from django.db import models
from django.utils import timezone

# user model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# model for the user
# https://www.youtube.com/watch?v=c-SVweZiiKs
# https://docs.djangoproject.com/en/3.2/topics/db/examples/one_to_one/

"""class Student(models.Model):
    '''
    Student profile
    '''
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    ) # links user with info

    existing_user = models.BooleanField(default=True)
    def __str__(self):
        return self.user.username"""


# model that holds data for an assignment
# assignment has a field that stores id of user that created it

class Assignment(models.Model):
    """
    This model is user specific (each user has their own assignments)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # primary
    #primary key?
    course = models.CharField(max_length=200, default="class")
    title = models.CharField(max_length=200, default="assignment name")
    description = models.CharField(max_length=200, default="description")
    date_created = models.DateTimeField('date created', default=timezone.now())
    due_date = models.DateTimeField('due date', default=timezone.now())

    def __str__(self):
        return self.title



# class model have a many to many field
# joining table
# class.user_set filter by user id and class id
# https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/
# c1 = getobject get class name and
# publication is User other thing is class

"""@receiver(post_save, sender=User, dispatch_uid="create_user")
def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
    instance.profile.save()

@receiver(post_save, sender=User, dispatch_uid="link_user_to_student")
def user_to_student(sender, instance, **kwargs):
    instance.student.save()"""