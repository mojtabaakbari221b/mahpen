# Generated by Django 4.0 on 2022-04-12 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_profile',
            field=models.ImageField(blank=True, upload_to='user/profile'),
        ),
    ]
