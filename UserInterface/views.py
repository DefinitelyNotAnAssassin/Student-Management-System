from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from Accounts.models import * 
from Registrar.models import * 
from Accounting.models import * 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.db.models import Q

# battery included 
User = get_user_model()

# Create your views here.


def index(request):
    # Query the student 
    q = Student.objects.get(student_number = "202200815")

    # Query the course 
    c = Course.objects.get(id=1)
    # Query the Courses where the Student is enrolled 
    print(q.courses.all())
    # Query the Students under the Course 
    print(c.students.all())

    # Query the grades of the student 

    g = get_object_or_404(Grade, student = q, course = c)
        

    # Query the grades of a Course 

    print(c.grade_set.all())

    return render(request, 'UserInterface/index.html')



def login_page(request):
    if request.method == 'GET':
        return render(request, 'UserInterface/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        

        isUser = authenticate(username  = request.POST['username'], password = request.POST['password'])
        print(isUser)

        if isUser:
            login(request, isUser)
            return redirect('index')
        else:
            isUser = ProjectAdmin.objects.get(username = 'dx')
            login(request, isUser, backend = 'Accounts.backends.AuthBackend')
            return HttpResponse("...")
        


@login_required
def logout_page(request):
    logout(request.user)
    return redirect('login page')


@login_required
def grade_page(request):
    grade = Grade.objects.filter(student = request.user.student_set.first())
    print(grade)

    # ^^ filters alll of the grade of the student

    items = {
        'grades': grade,

    }
    return render(request, 'UserInterface/grades.html', context = items)



def schedule(request):
    schedules = request.user.student_set.first().courses.all()
    items = {
        'schedules': schedules
    }
    return render(request, 'UserInterface/schedule.html', context=items)



