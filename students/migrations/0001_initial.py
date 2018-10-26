# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-10-25 10:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rollno', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('dob', models.DateField()),
                ('branch', models.CharField(choices=[('Computer Science and Engineering', 'Computer Science and Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Aeronautical Engineering', 'Aeronautical Engineering')], max_length=50)),
                ('session', models.CharField(choices=[('2017-18', '2017-18'), ('2018-19', '2018-19'), ('2019-20', '2019-20')], default='2018-19', max_length=7)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('aadhar', models.CharField(blank=True, max_length=12, null=True, unique=True)),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('fees_paid', models.IntegerField()),
                ('pending_fees', models.IntegerField(blank=True, null=True)),
                ('fully_paid', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('year', models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')], default=1)),
                ('roomno', models.CharField(blank=True, max_length=5, null=True)),
                ('bedno', models.CharField(blank=True, max_length=1, null=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]