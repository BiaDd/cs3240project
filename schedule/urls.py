from django.urls import path

from . import views


app_name = 'schedule'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('assignment', views.AssignmentView.as_view(), name='assignment'),
    path('assignment/list', views.AssignmentList.as_view(), name='assignmentlist'),
    path('submit_assignment', views.submit_assignment, name='submitthought'),
]