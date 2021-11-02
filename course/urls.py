from django.urls import path
from .views import CourseListView, CourseFormView, CourseDetailView

app_name = 'course'
urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='detail'),
    path('form/', CourseFormView.as_view(), name='form'),
]
