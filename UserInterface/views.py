from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from Accounts.models import * 
from Registrar.models import * 
from Accounting.models import * 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.db.models import Q

from django.contrib.auth.hashers import make_password

# battery included 
User = get_user_model()

# Create your views here.


def index(request):
   
    return render(request, 'UserInterface/index.html')



def login_page(request):
    if request.method == 'GET':
        return render(request, 'UserInterface/login.html')
    elif request.method == 'POST':
        isUser = authenticate(username  = request.POST['username'], password = request.POST['password'])
        print(isUser)

        if isUser:
            login(request, isUser)
            return redirect('index')
        else:
          
            return HttpResponse("...")
        


@login_required
def logout_page(request):
    logout(request)
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
        'schedules': schedulse
    }
    return render(request, 'UserInterface/schedule.html', context=items)



