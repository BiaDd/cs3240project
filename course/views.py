from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Course
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CourseForm

class CourseListView(generic.ListView):
    template_name = 'course/course_list.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        user_info = self.request.user
        cur_user = User.objects.get(username=user_info.username, email=user_info.email)
        return cur_user.course_set.all()

class CourseDetailView(generic.DetailView):
    model = Course

class CourseFormView(generic.FormView):
    template_name = 'course/course_form.html'
    form_class = CourseForm

    def form_valid(self, form):
        user_info = self.request.user
        course_name = form.cleaned_data.get('course_name')
        cur_user = User.objects.get(username=user_info.username, email=user_info.email)

        course, created = Course.objects.get_or_create(course_name=course_name)
        course.users.add(cur_user)
        return HttpResponseRedirect(reverse('course:list'))
