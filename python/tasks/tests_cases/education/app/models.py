from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Product(models.Model):
    title = models.CharField(max_length=100, 
                            verbose_name='title',
                            help_text='title product',
                            default='title')
    slug = models.SlugField(max_length=100, 
                            unique=True, 
                            verbose_name='slug name',
                            help_text='slug view')
    owner = models.ForeignKey(User, 
                            related_name='product_created',
                            on_delete=models.CASCADE)
    permiss = models.BooleanField(default=False, 
                            verbose_name='permissions_for_user',
                            help_text='permission')
    
    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title

class Lesson(models.Model):
    lesson_to_product = models.ForeignKey(Product, 
                            related_name='lessons', 
                            on_delete=models.CASCADE)
    name_of_lesson = models.CharField(max_length=100,
                            verbose_name='name_of_lesson',
                            help_text='name of lesson',
                            default='title')
    video = models.URLField(max_length=400, 
                            help_text='url for video')
    duration = models.FloatField(help_text='duration video in sec')
    visited = models.BooleanField(default=False, 
                                    help_text='show video')
    current_time = models.FloatField(help_text='durration video visited')
    users = models.ManyToManyField(User, 
                                    related_name='buy_of_lesson',   
                                    blank=True)
    last_time = models.DateField(auto_now_add=False)
    
    def __str__(self):
        return self.name_of_lesson

class Content(models.Model):
    lessons = models.ForeignKey(Lesson,
                        related_name='video_for_lessons', 
                        on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, 
                        on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')

