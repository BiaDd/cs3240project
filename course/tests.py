from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Course, Document
from .forms import DocumentForm
from django.core.files.uploadedfile import SimpleUploadedFile


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

class FileUploadTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', email='test@testing.com',password='chonkycookies123')
        self.client = Client()
        self.client.login(username='test',password='chonkycookies123')
        
    
    def test_upload_file(self):
        
        # Add in a course first
        self.client.post('/course/form/', data={'course_name':'cs3240'})
        course_added = Course.objects.get(course_name='CS3240')
        
        # Upload a pdf for the course
    
        self.client.post('course:upload', {'docfile' : SimpleUploadedFile('randomnotes.pdf',b'random content in pdf', content_type='application/pdf')})
        response = self.client.get('/course/'+str(course_added.course_name)+'/notes/')

        # Get the DocumentForm from the response
        docfile_field = response.context['form']
        doc = docfile_field.save(commit=False) # save it into a Document
        doc.course = course_added # Make sure that Document's course field is the course that was added
        doc.save() # save the Document
        self.assertEqual(str(doc.course), 'CS3240') # Check to see if the Document belongs to the appropriate course
    
        self.assertEqual(str(doc.docfile.name), 'randomnotes.pdf') # Check to see if the pdf doc has been uploaded
        


