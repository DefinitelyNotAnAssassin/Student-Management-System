# Generated by Django 4.2.7 on 2023-11-17 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registrar', '0004_course_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.IntegerField(choices=[(1, '1st Semester'), (2, '2nd Semester')], default=1),
            preserve_default=False,
        ),
    ]
