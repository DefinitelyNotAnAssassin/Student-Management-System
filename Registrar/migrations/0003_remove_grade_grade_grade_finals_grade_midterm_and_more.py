# Generated by Django 4.2.7 on 2023-11-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registrar', '0002_auto_20231112_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='grade',
        ),
        migrations.AddField(
            model_name='grade',
            name='finals',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='midterm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='prelim',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
