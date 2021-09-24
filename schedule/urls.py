from django.urls import path

from . import views


app_name = 'schedule'
urlpatterns = [
    path('', views.index, name='index'),
    path('assignment/create', views.assignment_form, name='assignment_form'),
    path('assignment/list', views.AssignmentListView.as_view(), name='assignmentlist'),
    path('submit_assignment', views.create_assignment, name='create_assignment'),
]
