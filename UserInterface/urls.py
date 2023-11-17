from django.urls import path 
from UserInterface import views

urlpatterns = [


    path('', views.index , name = 'index'),
    path('login', views.login_page, name='login page'),
    path('logout', views.logout_page, name = 'logout page'),
    path('grade', views.grade_page, name = 'grade page'),
    path('schedule', views.schedule, name ='schedule page')
    
    
]