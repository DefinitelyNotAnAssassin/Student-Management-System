# Generated by Django 4.2.7 on 2023-11-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_projectadmin_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
    ]
