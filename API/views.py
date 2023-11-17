from django.shortcuts import render, HttpResponse, get_object_or_404, redirect 
from django.http import JsonResponse
from Accounts.models import * 
from Registrar.models import *
from django.views.decorators.csrf import csrf_exempt
from API.forms import EditCourseForm
from django.contrib.auth.hashers import make_password
import json 
# Create your views here.

def check_enrolled(student, course):
    enrolled = student.courses.all().contains(course)
    print(enrolled)
    if enrolled:
        return True
    else:
        return False
def editable_student(request):
    if request.method == "GET":
        s = get_object_or_404(Student, id = request.GET.get('id'))
        return HttpResponse(f"""
<div id="modal" _="on closeModal add .closing then wait for animationend then remove me">
	<div class="modal-underlay" _="on click trigger closeModal"></div>
	<div class="modal-content">
        <form  hx-post = '/api/edit_student' hx-trigger = 'submit' hx-target = 'body'>  
              
                <label for = 'student_number'> Student Number </label>
                <input autocomplete = 'off' class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type = 'text' name = 'student_number' value = {s.student_number} />
                <label for = 'first_name'> First Name </label>
                <input autocomplete = 'off' class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type = 'text' name = 'first_name' value = {s.account.first_name} />
                <label for = 'last_name'> Last Name </label>
                <input autocomplete = 'off' class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type = 'text' name = 'last_name' value = {s.account.last_name} />
                <label for = 'address'> Address </label>
                <input autocomplete = 'off' class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" type = 'text' name = 'address' value = {s.address} />
                <input name = 'id' type = 'hidden' value = '{s.account.identifier}'/>

        
		<button _="on click trigger closeModal" class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded" type = 'submit' > Save </button>
		<a _="on click trigger closeModal" class="bg-transparent hover:bg-red-500 text-red-700 font-semibold hover:text-white py-2 px-4 border border-red-500 hover:border-transparent rounded"> Close </a> 
        </form>
	</div>
</div>
""")
    else:
        return HttpResponse("Invalid Method")
                            
@csrf_exempt
def edit_student(request):
    if request.method == 'POST':
        print(request.POST['id'])
        s = get_object_or_404(Student, account__identifier = request.POST['id']) # FIX, vulnerable for html edit, create some custome auth
        print(s.account.first_name)
        
        s.student_number = request.POST['student_number']
        
        s.account.first_name = request.POST['first_name']
        s.account.last_name = request.POST['last_name']
        s.address = request.POST['address']
        s.save()
        s.account.save()
        
        print("Saved")


        return redirect('manage students')


def add_student(request):
    if request.method == 'GET':
        return render(request, 'AdminInterface/modal.html')
    elif request.method == 'POST':
        data = request.POST
        print("...")
        add_account = ProjectAdmin(username = data['username'], password = make_password(data['password']), first_name = data['first_name'], last_name = data['last_name'])
        add_student = Student(account = add_account, student_number = data['student_number'], address = data['address'])
        print("...")
        add_account.save()
        add_student.save()
        print("...")
        return redirect('manage students')
    

def editable_course(request):
    id = request.GET.get('id')
    c = get_object_or_404(Course, id = id)
    form = EditCourseForm(instance = c)
    
    # form.faculty.queryset = TODO 
    print(c.students.all())
    items = {
        'id' : c.identifier,
        'form': form,

    }
    return render(request, 'AdminInterface/course_edit_modal.html', context=items)




@csrf_exempt
def edit_course(request):
    if request.method == 'POST':
        data = request.POST 
        print(data)
        c = get_object_or_404(Course, identifier = data['id'])
        c.course_name = data['course_name']
        for student in data.getlist('students'):
            s = get_object_or_404(Student, student_number = student)
            if not check_enrolled(s, c):
                c.students.add(s)
                g = Grade(student = s, course = c)
                g.save()

                print("Student Added")
        c.save()
        return redirect(f'/lmsadmin/manage_courses/?semester={c.semester}&academic_year={c.academic_year}')
    

@csrf_exempt
def filter_students(request):
    if request.method == 'POST':
      
        return HttpResponse("...")
    
    if request.method == 'GET':
        id = request.GET['id']
        c = get_object_or_404(Course, identifier = id)
        s = Student.objects.filter(student_number__icontains = request.GET['q']).exclude(student_number__in = c.students.all().values_list('student_number')).values_list('student_number', 'student_number')
        
        return HttpResponse(json.dumps(dict(s)))