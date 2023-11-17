from django import template
from Registrar.models import * 

register = template.Library()



# Method or Filters? Not every instance will benefit from <student_qs>.grades(course) and will not be implemented 
# inside the django template 

def get_grade(student, course):
    g = Grade.objects.filter(student = student, course = course)
    return g


register.filter("get_grade", get_grade)