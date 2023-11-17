from django.contrib import admin
from Accounts import models
# Register your models here.
admin.site.register(models.Accountant)
admin.site.register(models.Faculty)
admin.site.register(models.Student)
admin.site.register(models.Registrar)
admin.site.register(models.ProjectAdmin)