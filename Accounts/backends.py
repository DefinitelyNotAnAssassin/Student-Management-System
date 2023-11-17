from Accounts.models import ProjectAdmin
from django.db.models import Q 



class AuthBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = False
    supports_inactive_user = False


    def get_user(self, user_id):
       try:
          return ProjectAdmin.objects.get(id=user_id)
       except ProjectAdmin.DoesNotExist:
      
          return None


    def authenticate(self,request, username, password):
        print(username)
        print(password)
        try:
            
            user = ProjectAdmin.objects.get(
                Q(student__student_number=username) | Q(faculty__faculty_number=username) | Q(registrar__faculty_number=username)
            )
        except ProjectAdmin.DoesNotExist:
    
            return None
    
        return user if user.check_password(password) else None