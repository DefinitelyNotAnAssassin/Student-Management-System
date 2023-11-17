from django.urls import path 
from API import views


urlpatterns = [

    path('editable_student', views.editable_student, name='editable student'),
    path('edit_student', views.edit_student, name='edit student'),
    path('add_student', views.add_student, name='add student'),
    path('editable_course', views.editable_course, name='editable course'),
    path('edit_course', views.edit_course, name='edit course'),
    path('filter_students', views.filter_students, name = 'filter students'),

]