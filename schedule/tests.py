import datetime
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Course, Assignment


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

class CourseTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', email='test@testing.com', password='password')
        self.client = Client()
        self.client.login(username='test', password='password')

    def test_create_course(self):
        self.client.post('/course/form/', data={'course_name':'sts1500'})
        self.client.post('/course/form/', data={'course_name':'cs3240'})
        self.client.post('/course/form/', data={'course_name':'dracula'})

        course_list = self.user.course_set.values_list('course_name', flat=True)
        self.assertSequenceEqual(course_list, ['sts1500', 'cs3240', 'dracula'])

    # def test_course_list(self):
        # response = self.client.get('/course/')
        # self.assertSequenceEqual()
        # c.post('/course/test/', data={'course_name':'sts1500'})
        # c.post('/course/test/', data={'course_name':'cs3240'})
        # c.post('/course/test/', data={'course_name':'dracula'})

    # def test_user_list_in_course(self):
        # hi


    # def test_signup_course(self):
        # hi



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
