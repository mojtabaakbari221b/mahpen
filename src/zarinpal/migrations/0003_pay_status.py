# Generated by Django 4.0 on 2022-02-11 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zarinpal', '0002_alter_pay_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='status',
            field=models.PositiveIntegerField(default=103),
            preserve_default=False,
        ),
    ]