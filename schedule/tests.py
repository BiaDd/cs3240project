import datetime
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from .models import Assignment, Course


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

def createAssignment(user, course, title, description,  due_date):

    return Assignment.objects.create(user=user, course=course, title=title, description=description, date_created=timezone.now(), due_date=due_date)

class AssignmentCreationTest(TestCase):
    def setUp(self):
        s = "do nothing"

    def testCreate(self):
        # Creates a new assignment and verifies it was saved in the database
        User = get_user_model()
        user = User.objects.create(username="testing_user")
        user.set_password("password")
        user.save()
        c = Client()
        c.login(username="testing_user", password="password")

        createAssignment(user = user, course = "test_course", title = "test_title",
                         description="test_desc", due_date = timezone.now()+datetime.timedelta(days=5))
        query = Assignment.objects.get(title="test_title")
        self.assertTrue(query)


        """
        response = c.post('/assignment/create/', {'course':'test_course', 'title':'test_title', 'desc':'test_desc',
                                                  'due_date':timezone.now()+datetime.timedelta(days=5)},  follow=True)
        self.assertEqual(response.status_code, 200)"""


    """
    def testCreateNotLoggedIn(self):
        # Verifies that an exception occurs if a user tries to submit an assignment without logging in (we should solve this by redirecting users to log in first)
        c = Client()
        """


# --------------------------------------------- Sprint 4 test cases
"""def createCourse(coursetitle, user):
    return Course.objects.create(course=coursetitle, users=user)

class CourseTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create(username="testing_user")
        user.set_password("password")
        user.save()
        c = Client()
        c.login(username="testing_user", password="password")


    def test_course_list(self):
        response = self.client.get(reverse('course'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No course, sign up for a new course!")


    def test_create_course(self):
        # Enroll test
        User = get_user_model()
        user = User.objects.create(username="testing_user")
        user.set_password("password")
        user.save()
        c = Client()
        c.login(username="testing_user", password="password")

        return createCourse(coursetitle="test_course", user=user)


    #test to sign up for a course
    def test_signup_course(self):
        User = get_user_model()
        user = User.objects.create(username="testing_user")
        user.set_password("password")
        user.save()
        c = Client()
        c.login(username="testing_user", password="password")
        createCourse(coursetitle="test_course", user=user)

        Course.users = user # not sure if this is right


    # check to see if a signed-up student is on the roster
    def test_user_list_in_course(self):
        User = get_user_model()
        user = User.objects.create(username="testing_user")
        user.set_password("password")
        user.save()
        c = Client()
        c.login(username="testing_user", password="password")

        course = createCourse(coursetitle="test_course", user=user)

        response = self.client.get(reverse('course:index'))"""

    """
