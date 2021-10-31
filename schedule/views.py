from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Assignment, Course
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required # used to redirect users to login page
from django.utils import timezone
from .forms import CourseForm


def index(request):
    return render(request, 'schedule/index.html')

class IndexView(generic.ListView):
    template_name = 'schedule/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Assignment.objects.order_by('-due_date')[:5]

def assignment_form(request):
    return render(request, 'schedule/assignment_form.html')

class AssignmentListView(generic.ListView):
    template_name = 'schedule/assignment_list.html'
    context_object_name = 'assignment_list'

    def get_queryset(self):
        return Assignment.objects.filter(user_id=self.request.user.id)


def create_assignment(request):
    if (request.method == 'POST'):
        course = request.POST["course"]
        title = request.POST["title"]
        desc = request.POST["desc"]
        due_date = request.POST["due_date"]
        if (not course or not title or not desc or not due_date):
            return render(request, 'schedule/assignment_form.html', {
                'error_message': "Please fill out the text boxes.",
            })
        Assignment.objects.create( # when assignment is created,
            user_id = request.user.id, # user id associated with this assignment is set to current user
            course = course,
            title = title,
            description = desc,
            date_created = timezone.now(),
            due_date = due_date
        )
    return HttpResponseRedirect(reverse('schedule:assignment_list'))

def delete_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    assignment.delete()
    return HttpResponseRedirect(reverse('schedule:assignment_list'))

#-------------------------------------------------------------------------------
# Course specific views
class CourseListView(generic.ListView):
    template_name = 'schedule/course_list.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        user_info = self.request.user
        cur_user = User.objects.get(username=user_info.username, email=user_info.email)
        return cur_user.course_set.all()

class CourseDetailView(generic.DetailView):
    model = Course

class CourseFormView(generic.FormView):
    template_name = 'schedule/course_form.html'
    form_class = CourseForm

    def form_valid(self, form):
        user_info = self.request.user
        course_name = form.cleaned_data.get('course_name')
        cur_user = User.objects.get(username=user_info.username, email=user_info.email)

        course, created = Course.objects.get_or_create(course_name=course_name)
        course.users.add(cur_user)
        return HttpResponseRedirect(reverse('course_list'))

"""
def Enroll(request):
    if (request.method == 'POST'):
        course_name = request.POST["True"] # if user decides to enroll in course
        if (not course_name): # if doesn't decide, can't enroll
            return render(request, 'schedule/assignment_form.html', {
                'error_message': "Please fill out the course name.",
            })
        Course.objects.create(
            users = request.user.id,
            course = request.course.id
        )
        return HttpResponseRedirect(reverse('schedule:course_list'))


# this may seem useless now, but it can show a log of users who joined the class!
class EnrollmentListView(generic.ListView):
    template_name = 'schedule/course_list.html'
    context_object_name = 'enrollment'

    def get_queryset(self):
        return Course.objects.all()"""
