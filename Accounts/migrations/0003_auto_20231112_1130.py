# Generated by Django 3.2.6 on 2023-11-12 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_remove_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountant',
            name='name',
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='name',
        ),
        migrations.RemoveField(
            model_name='registrar',
            name='name',
        ),
    ]
