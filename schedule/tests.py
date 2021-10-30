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

"""
def createAssignment(user, course, title, description, date_created, due_date):

    return Assignment.objects.create(user=user, course=course, title=title, description=description, date_created=date_created, due_date=due_date)
class AssignmentCreationTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create(username="testing_user")
        user.set_password("password")
        user.save()

    def testCreate(self):
        # Creates a new assignment and verifies it was saved in the database
        c = Client()
        c.login(username="testing_user", password="password")
        response = c.post('/organizer/submit/', {'title':'test', 'deadline':timezone.now()+datetime.timedelta(hours=5)}, follow=True)
        self.assertEqual(response.status_code, 200)
        query = Assignment.objects.get(title="test")
        self.assertTrue(query)

    def testCreateNotLoggedIn(self):
        # Verifies that an exception occurs if a user tries to submit an assignment without logging in (we should solve this by redirecting users to log in first)
        c = Client()
        self.assertRaises(TypeError, c.post('/organizer/submit', {'title':'test2', 'deadline':timezone.now()+datetime.timedelta(hours=5)}))"""