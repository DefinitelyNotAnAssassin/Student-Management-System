# Generated by Django 4.2.7 on 2023-11-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registrar', '0003_remove_grade_grade_grade_finals_grade_midterm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='identifier',
            field=models.UUIDField(null=True),
        ),
    ]
