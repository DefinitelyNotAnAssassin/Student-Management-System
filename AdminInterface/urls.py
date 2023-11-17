from django.urls import path 
from AdminInterface import views

urlpatterns = [
    path('lmsadmin/dashboard/', views.admin_dashboard, name = 'admin dashboard'),
    path('lmsadmin/manage_students/', views.manage_students, name = 'manage students'),
    path('lmsadmin/manage_faculty/', views.manage_faculty, name = 'manage faculty'),
    path('lmsadmin/manage_courses/', views.manage_courses, name = 'manage courses'),
    path('lmsadmin/manage_records/', views.manage_records, name = 'manage recoeds'),
    path('lmsadmin/manage_schedule/', views.manage_schedule, name = 'schedule page'),
    path('lmsadmin/logout/', views.logout, name = 'admin dashboard'),
    path('lmsadmin/view_course/<uuid:identifier>', views.view_course, name = 'view course'),
]
