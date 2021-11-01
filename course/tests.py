from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Course

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

    def test_course_list(self):
        self.client.post('/course/form/', data={'course_name':'sts1500'})
        self.client.post('/course/form/', data={'course_name':'cs3240'})
        self.client.post('/course/form/', data={'course_name':'dracula'})

        response = self.client.get('/course/')
        self.assertContains(response, 'sts1500')
        self.assertContains(response, 'cs3240')
        self.assertContains(response, 'dracula')

    def test_user_list_in_course(self):
        self.client.post('/course/form/', data={'course_name':'sts1500'})
        get_user_model().objects.create_user(username='other', email='other@testing.com', password='password')
        self.client.login(username='other', password='password')
        self.client.post('/course/form/', data={'course_name':'sts1500'})
        course_added = Course.objects.get(course_name='sts1500')

        response = self.client.get('/course/' + str(course_added.pk) +'/')
        self.assertContains(response, 'test')
        self.assertContains(response, 'other')

    def test_signup_course(self):
        Course.objects.create(course_name='cs3240')
        old_len = len(Course.objects.all())
        self.client.post('/course/form', data={'course_name':'cs3240'})
        new_len = len(Course.objects.all())
        self.assertEqual(old_len, new_len)
