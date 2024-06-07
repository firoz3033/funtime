# Generated by Django 5.0.4 on 2024-06-02 11:19

import django.db.models.deletion
import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=100)),
                ('courseDesc', models.CharField(max_length=200)),
                ('courseAuthor', models.CharField(max_length=100)),
                ('courseStartDate', models.DateField()),
                ('courseEndDate', models.DateField()),
                ('courseLanguage', models.CharField(max_length=100)),
                ('coursePrice', models.CharField(max_length=10)),
                ('courseDisPrice', models.CharField(max_length=10)),
                ('courseDetails', tinymce.models.HTMLField()),
                ('courseFeatureImg', models.FileField(default=None, max_length=250, null=True, upload_to='course/')),
                ('courseTagImg', models.FileField(default=None, max_length=250, null=True, upload_to='course/')),
            ],
        ),
        migrations.CreateModel(
            name='enquiryform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enquiryform_firstName', models.CharField(max_length=50)),
                ('enquiryform_lastName', models.CharField(max_length=50)),
                ('enquiryform_email', models.EmailField(max_length=50)),
                ('enquiryform_number', models.CharField(max_length=50)),
                ('enquiryform_msg', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='registered_Students',
            fields=[
                ('firstName', models.CharField(max_length=80)),
                ('lastName', models.CharField(max_length=80)),
                ('fatherName', models.CharField(max_length=150)),
                ('motherName', models.CharField(max_length=150)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('registration_number', models.CharField(max_length=12)),
                ('student_number', models.CharField(max_length=12)),
                ('parent_number', models.CharField(max_length=12)),
                ('passed_class', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('image', models.FileField(default=None, max_length=250, null=True, upload_to='students/')),
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_name', models.CharField(max_length=50)),
                ('testimonial_role', models.CharField(max_length=50)),
                ('testimonial_para', models.CharField(max_length=150)),
                ('testimonial_Img', models.FileField(default=None, max_length=250, null=True, upload_to='testimonial/')),
            ],
        ),
        migrations.CreateModel(
            name='students_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(max_length=50)),
                ('result_of_reg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sankalp.registered_students')),
            ],
        ),
    ]