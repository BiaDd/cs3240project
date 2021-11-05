from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Course, Document
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import CourseForm, DocumentForm


class CourseListView(generic.ListView):
    template_name = 'course/course_list.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        user_info = self.request.user
        cur_user = User.objects.get(username=user_info.username, email=user_info.email)
        return cur_user.course_set.all()

class CourseDetailView(generic.DetailView):
    model = Course

    def get_object(self, queryset=None):
        return Course.objects.get(course_name=self.kwargs.get("course_name"))

class CourseFormView(generic.FormView):
    template_name = 'course/course_form.html'
    form_class = CourseForm

    def form_valid(self, form):
        user_info = self.request.user
        course_name = form.cleaned_data.get('course_name').upper()
        cur_user = User.objects.get(username=user_info.username, email=user_info.email)

        course, created = Course.objects.get_or_create(course_name=course_name)
        course.users.add(cur_user)
        return HttpResponseRedirect(reverse('course:list'))


def UploadDocumentFormView(request):
    message = 'Upload Notes!'
    if request.method == 'POST': # if the request is POST
        form = DocumentForm(request.POST, request.FILES) # creates a document
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('course:upload'))
        else:
            message = 'invalid form:'
    else:
        form = DocumentForm()  # A empty, unbound form, if they don't post

    # Load documents for the list page
    #documents = Document.objects.filter(course=Course.objects.get_or_create(pk))
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message}
    return render(request, 'course/course_notes.html', context)
