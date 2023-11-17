from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.hashers import make_password
import uuid
# Create your models here.



class Student(models.Model):
    account = models.ForeignKey('ProjectAdmin', on_delete=models.CASCADE)
    student_number = models.CharField(max_length=64, unique=True)
    address = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=16, null = True)
    birthday = models.DateField(null = True, blank = True)
    program_id = models.ForeignKey('Registrar.Program', on_delete=models.CASCADE, null=True)
    level = models.IntegerField(null=True)
    other_information = models.TextField(null=True, blank = True, default="Other Information...")
    USERNAME_FIELD = "student_number"
    courses = models.ManyToManyField("Registrar.Course", related_name='students')

    def __str__(self):
        return f'{self.account.first_name}  {self.account.last_name} | {self.student_number}'
    
class Faculty(models.Model):
    account = models.ForeignKey('ProjectAdmin', on_delete=models.CASCADE)
    faculty_number = models.CharField(max_length=64, unique=True)
    def __str__(self):
        return f'{self.account.first_name}  {self.account.last_name} | {self.faculty_number}'
class Registrar(models.Model):
    account = models.ForeignKey('ProjectAdmin', on_delete=models.CASCADE)
    faculty_number = models.CharField(max_length=64, unique=True)
    
class Accountant(models.Model):
    account = models.ForeignKey('ProjectAdmin', on_delete=models.CASCADE)
    faculty_number = models.CharField(max_length=64, unique=True)
   



class ProjectAdmin(AbstractUser):
    is_student = models.BooleanField(default = False)
    is_faculty = models.BooleanField(default = False)
    is_registrar = models.BooleanField(default = False)
    is_accountant = models.BooleanField(default = False)
    identifier = models.UUIDField(default=uuid.uuid4)
    def save(self, *args, **kwargs):
        
        super(ProjectAdmin, self).save(*args, **kwargs)

  
    def __str__(self):
        return f'{self.username}'