from django.urls import path
from .views import CourseListView, CourseFormView, CourseDetailView, UploadDocumentFormView
from . import views
app_name = 'course'
urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('form/', CourseFormView.as_view(), name='form'),
    #path('<int:pk>/notes/', views.UploadDocumentFormView, name='upload'), # goes to the file list for class
    path('notes/', views.UploadDocumentFormView, name='upload'),
    path('<str:course_name>/', CourseDetailView.as_view(), name='detail'),
]
