# Generated by Django 4.0 on 2022-04-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_alter_course_supported_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='supported_course',
            field=models.ManyToManyField(blank=True, to='course.Course'),
        ),
    ]