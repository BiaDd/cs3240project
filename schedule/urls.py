from django.urls import path

from . import views


app_name = 'schedule'
urlpatterns = [
    path('', views.index, name='index'),
    path('assignment/form/', views.assignment_form, name='assignment_form'),
    path('assignment/list/', views.AssignmentListView.as_view(), name='assignment_list'),
    path('assignment/create', views.create_assignment, name='create_assignment'),
    path('assignment/delete/<int:assignment_id>', views.delete_assignment, name='delete_assignment'),
]
