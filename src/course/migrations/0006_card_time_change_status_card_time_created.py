# Generated by Django 4.0 on 2022-04-10 20:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='time_change_status',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='card',
            name='time_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
