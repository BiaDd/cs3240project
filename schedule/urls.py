from django.urls import path

from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


app_name = 'schedule'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path('accounts/', include('allauth.urls')),
    #path('logout', LogoutView.as_view()),
    path('assignment/form/', views.assignment_form, name='assignment_form'),
    path('assignment/list/', views.AssignmentListView.as_view(), name='assignment_list'),
    path('assignment/create', views.create_assignment, name='create_assignment'),
    path('assignment/delete/<int:assignment_id>', views.delete_assignment, name='delete_assignment'),
]