# Generated by Django 5.0.4 on 2024-06-10 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sankalp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial_Img',
            field=models.FileField(default=None, max_length=350, null=True, upload_to='testimonial/'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial_para',
            field=models.CharField(max_length=1000),
        ),
    ]
