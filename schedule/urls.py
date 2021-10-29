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
    #path('accounts/', include('allauth.urls')),
    #path('logout', LogoutView.as_view()),
    path('account/login', views.login, name='login'),
    path('assignment/form/', views.assignment_form, name='assignment_form'),
    path('assignment/list/', views.AssignmentListView.as_view(), name='assignment_list'),
    path('assignment/create', views.create_assignment, name='create_assignment'),
    path('assignment/delete/<int:assignment_id>', views.delete_assignment, name='delete_assignment'),
    path('course/list/', views.ClassListView.as_view(), name='course_list_view'),
]
