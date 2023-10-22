from django.db import models
import datetime

class TimeManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(vote_)

class Person(models.Model):
    your_name = models.CharField(max_length=50, 
                                verbose_name='persona name',
                                help_text='persona name')
    your_last_name = models.CharField(max_length=50, 
                                verbose_name='persona last name',
                                help_text='last name')
    your_father = models.CharField(max_length=40, 
                                verbose_name='father name',
                                help_text='father name')
    avatar = models.FileField(upload_to='avatars',
                                verbose_name='avatar',
                                help_text='avatar')
    age = models.IntegerField(default=18,
                                help_text='age persona')
    short_desc = models.TextField(default='',
                                max_length=400, 
                                help_text='About you...')
    def __str__(self):
        return self.your_name

class Vote(models.Model):

    name = models.CharField(max_length=60, 
                            verbose_name='name',
                            help_text='name of vote')
    begin = models.DateField(auto_now_add=False)
    end = models.DateField(auto_now=False)
    max_votes = models.IntegerField(default=40)
    persons = models.ForeignKey(Person, 
                                related_name='persons',
                                on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, help_text='active?')
        
    def __str__(self):
        return self.name

    

