from django.db import models

# Create your models here.
class BalanceStatement(models.Model):
    student_id = models.ForeignKey('Accounts.Student', on_delete=models.CASCADE)
    semester = models.IntegerField()
    academic_year = models.TextField(max_length=16)

    
    def __str__(self):
        return f"{self.student_id.name} | {self.semester} {self.academic_year}"
class Tuition(models.Model):
    program = models.ForeignKey('Registrar.Program', on_delete=models.CASCADE)
    year_level = models.IntegerField()
    academic_year = models.TextField(max_length=16) 
    installment = models.FloatField()
    full = models.FloatField()
     

    def __str__(self):
        return f"{self.program}-{self.year_level} {self.academic_year}"