from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Assignment


# Create your views here.
from django.http import HttpResponse


class IndexView(generic.ListView):
    template_name = 'schedule/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Assignment.objects.order_by('-pub_date')[:5]


def assignment_form(request):
    return render(request, 'schedule/assignment_form.html')

class AssignmentListView(generic.ListView):
    template_name = 'schedule/assignment_list.html'
    context_object_name = 'assignment_list'

    def get_queryset(self):
        return Assignment.objects.all()

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
        Assignment.objects.create(
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