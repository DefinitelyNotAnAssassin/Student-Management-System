from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from Accounts.models import * 
from Registrar.models import * 
from Accounting.models import * 
from uuid import uuid4
# Create your views here.


def faculty_checker(user):
    if user.is_faculty:
        return True
    
    else:
        return False

@login_required
def admin_dashboard(request):

    return render(request, 'AdminInterface/dashboard.html')




@login_required
def admin_dashboard(request):

    return render(request, 'AdminInterface/dashboard.html')

@login_required
def manage_students(request):
    Students = Student.objects.all()

    items = {
        'students': Students,

    }
    return render(request, 'AdminInterface/manage_students.html', context=items)


@login_required
def manage_faculty(request):
    faculties = Faculty.objects.all() 
    
    items = {
        'faculties': faculties,

    }
    return render(request, 'AdminInterface/manage_faculty.html', context=items)


@login_required
def manage_courses(request):
    if request.method == 'GET':
        return render(request, 'AdminInterface/manage_courses.html', )
    
    elif request.method == 'POST':
        c = Course.objects.filter(semester = request.POST['semester'])
        items = {
            'courses': c,
        }
        print(c)
        return render (request, 'AdminInterface/course_table.html', context = items)


@login_required
def manage_records(request):

    return render(request, 'AdminInterface/manage_records.html')

@login_required
def manage_schedule(request):
    s = Schedule.objects.all() 

    items = {
        'schedules': s,
    }
    return render(request, 'AdminInterface/manage_schedule.html', context=items)


@login_required
def logout_page(request):
    logout(request.user)
    return render(request, 'AdminInterface/dashboard.html')



@login_required 
def view_course(request, identifier):
    c = get_object_or_404(Course, identifier = identifier)
    items = {
        'course': c
    }
    return render (request, 'AdminInterface/view_course.html',context = items)



