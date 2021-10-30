import datetime
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Assignment


class UserTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create(username="testing_user")
        user.set_password("password")
        user.save()

    def testLogin(self):
        # Tests whether a user object is created
        c = Client()
        logged_in = c.login(username="testing_user", password="password")
        self.assertTrue(logged_in)

