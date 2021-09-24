from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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




class AssignmentView(generic.ListView):
    model = Assignment
    template_name = 'schedule/detail.html'


class AssignmentList(generic.ListView):
    template_name = 'schedule/assignmentlist.html'
    context_object_name = 'assignment_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Assignment.objects.order_by('title')


def submit_assignment(request):
    if (request.method == 'POST'):
        assignment_title = request.POST["title"]
        assignment_text = request.POST["thought"]
        date = request.POST["date"]
        if (not assignment_text or not assignment_title or not date):
            return render(request, 'schedule/detail.html', {
                'error_message': "Please fill out the text boxes.",
            })
        a = Assignment(title=assignment_title, assignment_text=assignment_text, pub_date=date)
        # print("boop beep", d.title, d.deepthought_text)
        a.save()

        return HttpResponseRedirect(reverse('schedule:assignmentlist'))