from django.contrib import admin
from .models import Assignment, Course


class AssignmentAdmin(admin.ModelAdmin):
    fields = ['user', 'course', 'title', 'description', 'date_created', 'due_date']

class CourseAdmin(admin.ModelAdmin):
    fields = ['course_name']

class EnrollAdmin(admin.ModelAdmin):
    fields = ['student', 'course', 'date_enrolled']

admin.site.register(Assignment, AssignmentAdmin)

admin.site.register(Course, CourseAdmin)
