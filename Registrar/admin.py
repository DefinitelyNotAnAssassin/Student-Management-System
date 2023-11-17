from django.contrib import admin
from Registrar import models 
# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.Program)
admin.site.register(models.Schedule)
admin.site.register(models.ScheduleSlot)
admin.site.register(models.Grade)