from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Assignment, Course
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required # used to redirect users to login page
from django.utils import timezone


def index(request):
    return render(request, 'schedule/index.html')

# planning to let a user see assignments in a small tab on their page, not all of them maybe just almost due ones
# so keeping it as listView might help
class IndexView(generic.ListView):
    template_name = 'schedule/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Assignment.objects.order_by('-due_date')[:5]

# homepage view
def homepage(request):
    return render(request, 'schedule/homepage.html')

#assignment form view
@login_required # this makes sure they are signed in
def assignment_form(request):
    #student .get object? get the user primary key, if not existing redirects to sign up
    # there's actually a header thing that redirects if they aren't signed up
    return render(request, 'schedule/assignment_form.html')

# view for login
# need to overide login template
def login(request):
    return render(request, 'schedule/login.html')



def course_form(request):
    return render(request, 'schedule/course_form.html')


class AssignmentListView(generic.ListView):
    template_name = 'schedule/assignment_list.html'
    context_object_name = 'assignment_list'

    def get_queryset(self):
        return Assignment.objects.filter(user_id=self.request.user.id)


#need to make sure login
@login_required
def create_assignment(request):
    if (request.method == 'POST'):
        course = request.POST["course"]
        title = request.POST["title"]
        desc = request.POST["desc"]
        due_date = request.POST["due_date"]
        if (not course or not title or not desc or not due_date):
            return render(request, 'schedule/detail.html', {
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


@login_required
def CreateClass(request):
    if (request.method == 'POST'):
        course_name = request.POST["course"]
        user_info = request.user
        cur_user = User.objects.get(username=user_info.username, email=user_info.email)
        print('username', request.user.username)
        print('email' + request.user.email)
        if (not course_name):
            return render(request, 'schedule/detail.html', {
                'error_message': "Please fill out the course name.",
            })
        new_course = Course.objects.create(course_name = course_name)
        new_course.users.add(cur_user)
        return HttpResponseRedirect(reverse('schedule:course_list_view'))


class ClassListView(generic.ListView):
    template_name = 'schedule/course_list.html'
    context_object_name = 'course_list_view'

    def get_queryset(self):
        user_info = self.request.user
        cur_user = User.objects.get(username=user_info.username, email=user_info.email)

        return cur_user.course_set.all()



@login_required
def Enroll(request):
    if (request.method == 'POST'):
        course_name = request.POST["True"] # if user decides to enroll in course
        if (not course_name): # if doesn't decide, can't enroll
            return render(request, 'schedule/detail.html', {
                'error_message': "Please fill out the course name.",
            })
        Course.objects.create(
            users = request.user.id,
            course = request.course.id
        )
        return HttpResponseRedirect(reverse('schedule:course_list'))


"""# this may seem useless now, but it can show a log of users who joined the class!
class EnrollmentListView(generic.ListView):
    template_name = 'schedule/course_list.html'
    context_object_name = 'enrollment'

    def get_queryset(self):
        return Course.objects.all()"""
