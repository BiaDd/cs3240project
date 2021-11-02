from django import forms

class CourseForm(forms.Form):
    course_name = forms.CharField(max_length=200)
