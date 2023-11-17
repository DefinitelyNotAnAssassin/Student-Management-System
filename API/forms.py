from django.forms import ModelForm, ModelMultipleChoiceField
from Accounts.models import * 
from Registrar.models import * 





class EditCourseForm(ModelForm):
    

    class Meta:
        model = Course  
        fields = ['course_schedule', 'course_name', 'program', 'course_schedule', 'faculty']
  
       