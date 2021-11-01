from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    fields = ['course_name', 'users']

admin.site.register(Course, CourseAdmin)

