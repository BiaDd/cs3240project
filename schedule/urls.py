from django.urls import path

from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.conf import settings

app_name = 'schedule'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('assignment/form/', views.assignment_form, name='assignment_form'),
    path('assignment/list/', views.AssignmentListView.as_view(), name='assignment_list'),
    path('assignment/create', views.create_assignment, name='create_assignment'),
    path('assignment/delete/<int:assignment_id>', views.delete_assignment, name='delete_assignment'),
    path('assignment/sort_by_due_date/', views.AssignmentDueDateListView.as_view(), name='sort_assignment_list_due_date'),
    path('assignment/sort_by_date_created/', views.AssignmentDateCreatedListView.as_view(), name='sort_assignment_list_date_created'),
    path('assignment/sort_by_desc/', views.AssignmentDescListView.as_view(), name='sort_assignment_list_desc'),
    path('assignment/sort_by_title/', views.AssignmentTitleListView.as_view(), name='sort_assignment_list_title'),
    path('assignment/sort_by_course/', views.AssignmentCourseListView.as_view(), name='sort_assignment_list_course'),


]
