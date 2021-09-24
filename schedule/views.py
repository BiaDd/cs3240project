from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Assignment

def index(request):
    return render(request, 'index.html')

class AssignmentListView(generic.ListView):
    template_name = 'polls/assignment_list.html'
    context_object_name = 'assignment_list'

    def get_queryset(self):
        return Assignment.objects.all()

def create_assignment(request):
    return render(request, 'submission')
