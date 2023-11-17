from django.db import models
import uuid
# Create your models here.



class Program(models.Model):
    program_code = models.CharField(max_length=16)
    program_name = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.program_code} - {self.program_name}"
class Course(models.Model):
    course_code = models.CharField(max_length=16)
    course_name = models.CharField(max_length=64)
    course_schedule = models.ForeignKey("Schedule", on_delete=models.CASCADE)
    program = models.ForeignKey("Program", on_delete=models.CASCADE)
    faculty = models.ForeignKey("Accounts.Faculty", on_delete=models.CASCADE)
    identifier = models.UUIDField(null = True )
    choices = [(1, '1st Semester'), (2, '2nd Semester')]
    semester = models.IntegerField(choices=choices)

    academic_years = [("2022-2023", "2022-2023"), ("2023-2024", "2023-2024"), ("2024-2025", "2024-2025"), ("2025-2026", "2025-2026"), ]
    academic_year = models.CharField(choices = academic_years, max_length=16)
    def save(self, *args, **kwargs):
            
        if not self.identifier:
            self.identifier = uuid.uuid4()
        return super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.course_code} {self.course_name} - {self.program.program_name}"

        
class ScheduleSlot(models.Model):
    weekday = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.weekday} {self.start_time}-{self.end_time}"


class Schedule(models.Model):
    sched_code = models.CharField(max_length=32)
    schedule_slots = models.ManyToManyField(ScheduleSlot)

    def __str__(self):
        return f'{self.sched_code}'

class Grade(models.Model):
    student = models.ForeignKey('Accounts.Student', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    prelim = models.FloatField(default = 0, null = True, blank = True)
    midterm = models.FloatField(default = 0, null = True, blank = True)
    finals = models.FloatField(default = 0, null = True, blank = True)

    def __str__(self):
        return f"{self.student.student_number} - {self.course.course_code} - {self.prelim} | {self.midterm} | {self.finals}"