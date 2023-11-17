# Generated by Django 4.2.7 on 2023-11-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_auto_20231112_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectadmin',
            name='is_accountant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectadmin',
            name='is_faculty',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectadmin',
            name='is_registrar',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='projectadmin',
            name='is_student',
            field=models.BooleanField(default=False),
        ),
    ]
