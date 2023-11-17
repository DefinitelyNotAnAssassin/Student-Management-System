from django.forms import ModelForm 
from Registrar.models import Course


class SelectCourseForm(ModelForm):
    class Meta: 
        model = Course 
        fields = ['semester', 'academic_year']