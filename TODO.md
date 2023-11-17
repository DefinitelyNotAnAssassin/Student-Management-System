Coures 

coure_code
course_name 
course_schedule 
program
faculty (string representation)

MANAGE COURSES 

c.sched_code, c.program (SR),
schedule (SR), FK faculty, 


RESEARCH: 

Cost of transversing relationship
in django orm (e.g. is the whole
model loaded whole SSR)




MANAGE RECORD:

TODO 


Logout : [DONE]


HYPERSCRIPT IMPLEMENTATION 



Manage [Table]: 
    TODO: 
        implement edit MODAL [DONE]
        implement views for information [DONE] 
        implement for SCHEDULE 

Add [Table]:
    TODO:
        SCHEDULE:
            add verification if the current schedule conflict with existing schedule of a :
                STUDENT [ONGOING]
                COURSE [ONGOING]
                SCHEDULE CODE [ONGOING]
        STUDENT, FACULTY, ACCOUNTING, REGISTRAR:
            add a function that will initiate the user alongside with ProjectAdmin/Users [DONE]

    API:
        CRUD to All Accounts Table and FK, M2M




ADD Students COURSE [Priority]:
    TODO:
        API Calls for Dynamic Data Search:
            Course API [M2M_students__exclude]
            Student API [student_number]
        Dyanmic public facing UUID for Course Identification s[on-going]
            ...lmsadmin/manage_course 
            ...get /AdminInterface/course_edit_modal.html 
            ...POST filter, /api/student_filter 
                HTTP Head: 
                    {
                        'id' : 'public_facing_uuid_embedded_into_the_modal's_hidden_form_passed_by_ajax'
                    }
                . q = get_objects_or_404(Course, id = request.POST['id])
                return HttpResponse(""" 
                    .q query_set
                """)
                

Design Decision: 
    Filter Students vs Student Verification e.g. "Student is already enrolled in this course" 

    