from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


#from .models import Student
from .models import Assignment, Course, Enrollment


class AssignmentAdmin(admin.ModelAdmin):
    fields = ['user', 'course', 'title', 'description', 'date_created', 'due_date']

class CourseAdmin(admin.ModelAdmin):
    fields = ['course_name']

class EnrollAdmin(admin.ModelAdmin):
    fields = ['student', 'course', 'date_enrolled']

"""class StudentAdmin(admin.ModelAdmin):
    fields = ['username', 'email']""" # might need this later

# Now register the new UserAdmin...
#admin.site.register(Student, StudentAdmin)

admin.site.register(Assignment, AssignmentAdmin) #assignments

admin.site.register(Course, CourseAdmin) # courses

admin.site.register(Enrollment, EnrollAdmin)
