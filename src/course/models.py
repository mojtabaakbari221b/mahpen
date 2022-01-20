from statistics import mode
from django.db import models
from blog.models import Category
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .utilities.models_validatior import validate_video_extension

class Course(models.Model):
    title = models.CharField(max_length=1024)
    detail = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.PROTECT)
    off = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ]
    )
    image = models.ImageField(upload_to="course/image")
    date = models.DateTimeField(auto_now=True)

class Content(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to="content/image")
    title = models.CharField(max_length=1024)
    detail = RichTextField()
    video = models.FileField(upload_to="course/video", validators=[validate_video_extension])
    date = models.DateTimeField(auto_now=True)

class Commnet(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    text = models.CharField(max_length=1024)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    parent = models.ForeignKey('self' , related_name='parent_comment', null=True, on_delete=models.CASCADE)
    child = models.ForeignKey('self' , related_name='child_comment', null=True, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now=True)
