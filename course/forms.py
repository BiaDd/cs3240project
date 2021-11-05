from django import forms

class CourseForm(forms.Form):
    course_name = forms.CharField(max_length=200)

class DocumentUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField(label="Select file to upload")