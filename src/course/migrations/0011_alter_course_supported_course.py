# Generated by Django 4.0 on 2022-04-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_course_supported_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='supported_course',
            field=models.ManyToManyField(blank=True, null=True, to='course.Course'),
        ),
    ]
