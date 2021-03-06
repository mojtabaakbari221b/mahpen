# Generated by Django 4.0 on 2022-03-29 13:16

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0001_initial'),
        ('blog', '0002_video_category_color_category_text_color_post_auhtor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='auhtor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_management.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='date_publish',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(default='', upload_to='post/image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='is_promote',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='text',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='title',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]
