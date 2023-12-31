# Generated by Django 3.2.6 on 2023-11-12 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Registrar', '__first__'),
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tuition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_level', models.IntegerField()),
                ('academic_year', models.TextField(max_length=16)),
                ('installment', models.FloatField()),
                ('full', models.FloatField()),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registrar.program')),
            ],
        ),
        migrations.CreateModel(
            name='BalanceStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('academic_year', models.TextField(max_length=16)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.student')),
            ],
        ),
    ]
