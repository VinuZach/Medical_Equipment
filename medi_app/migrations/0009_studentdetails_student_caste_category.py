# Generated by Django 4.1.2 on 2022-10-14 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medi_app', '0008_remove_studentdetails_student_caste_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='student_caste_category',
            field=models.CharField(default='General', max_length=20),
        ),
    ]
