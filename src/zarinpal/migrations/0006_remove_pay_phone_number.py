# Generated by Django 4.0 on 2022-02-11 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zarinpal', '0005_alter_pay_authority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pay',
            name='phone_number',
        ),
    ]