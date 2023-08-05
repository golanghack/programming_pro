from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from taggit.managers import TaggableManager
import typing

from main.utils import (get_timestamp_path,
                        send_new_comment_notification)

class AdvUser(AbstractUser):
    """AdvUser 
    is_activated -> user is activated?
    send_messages -> user send messages?
    """ 

    is_activated = models.BooleanField(default=True,
                                    db_index=True, 
                                    verbose_name='Активирован?')
    send_messages = models.BooleanField(default=True,
                                    verbose_name='Отправльять сообщения о комментариях?')
    
    def delete(self, *args, **kwargs):
        for news in self.news_set.all():
            news.delete()
        super().delete(*args, *kwargs)
    class Meta(AbstractUser.Meta):
        pass


class Rubric(models.Model):
    name = models.CharField(max_length=20, 
                            db_index=True, 
                            unique=True,
                            verbose_name='Название рубрики')
    order = models.SmallIntegerField(default=0, 
                            db_index=True, 
                            verbose_name='Порядок рубрик')
    super_rubric = models.ForeignKey('SuperRubric',
                            on_delete=models.PROTECT, 
                            null=True, 
                            blank=True, 
                            verbose_name='Родительская рубрика')
    tags = TaggableManager()

    
class SuperRubricManager(models.Manager):
    """Super rubric manager""" 

    def get_queryset(self) -> typing.Callable:
        return super().get_queryset().filter(super_rubric__isnull=True)


class SuperRubric(Rubric):
    """Super rubric -> parrent rubric for rubrics children""" 

    objects = SuperRubricManager()
    def __str__(self) -> str:
        return self.name

    class Meta:
        proxy = True 
        ordering = ('order', 'name')
        verbose_name = 'Родительская рубрика'
        verbose_name_plural = 'Надрубрики'

class SubRubricManager(models.Manager):
    """Sub rubric manager""" 

    def get_queryset(self) -> typing.Callable:
        return super().get_queryset().filter(super_rubric__isnull=False)

class SubRubric(Rubric):
    """Subrubric -> child rubric from SuperRubric""" 

    objects = SubRubricManager()

    def __str__(self) -> str:
        return f'{self.super_rubric.name} -> {self.name}'

    class Meta:
        proxy = True
        ordering = ('super_rubric__order', 
                    'super_rubric__name', 
                    'order',
                    'name')
        verbose_name = 'Подрубрика'
        verbose_name_plural = 'Подрубрики'


class News(models.Model):
    rubric = models.ForeignKey(SubRubric, 
                                on_delete=models.PROTECT,
                                verbose_name='Рубрика')
    title = models.CharField(max_length=160, 
                                verbose_name='Заголовок новости')
    content = models.TextField(verbose_name='Новость')
    weight = models.FloatField(default=0, verbose_name='Рейтинг сложности')
    source = models.CharField(max_length=40, verbose_name='Источник')
    image = models.ImageField(blank=True,
                                upload_to=get_timestamp_path, 
                                verbose_name='Изображение')
    author = models.ForeignKey(AdvUser, 
                                on_delete=models.CASCADE,
                                verbose_name='Автор новости на сайте')
    is_active = models.BooleanField(default=True,
                                db_index=True,
                                verbose_name='Выводить как список?')
    created_at = models.DateTimeField(auto_now_add=True,
                                db_index=True, 
                                verbose_name='Опубликована')
    tags = TaggableManager()
    
    def delete(self, *args, **kwargs):
        for ai in self.additionalimage_set.all():
            ai.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Новость'
        ordering = ['-created_at']

class AdditionalImage(models.Model):
    """Model adding the images""" 

    new = models.ForeignKey(News,
                            on_delete=models.CASCADE,
                            verbose_name='Новость')
    image = models.ImageField(upload_to=get_timestamp_path,
                            verbose_name='Изображение')

    class Meta:
        verbose_name_plural = 'Иллюстрации к новости'
        verbose_name = 'Иллюстрация к новости'

class Comment(models.Model):
    """Comment model""" 

    new = models.ForeignKey(News, on_delete=models.CASCADE,
                                    verbose_name='Новость')
    author = models.CharField(max_length=20, 
                                    verbose_name='Автор')
    content = models.TextField(verbose_name='Комментарий')
    is_active = models.BooleanField(default=True, 
                                    db_index=True, 
                                    verbose_name='Показывать на экране?')
    created_at = models.DateTimeField(auto_now_add=True, 
                                    db_index=True, 
                                    verbose_name='Опубликован')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['created_at']

def post_save_manager(sender: str, **kwargs) -> typing.Callable:
    """Signal for save"""

    author = kwargs['instance'].new.author
    if kwargs['created'] and author.send_messages:
        send_new_comment_notification(kwargs['instance'])

#manager for post_save
post_save.connect(post_save_manager, sender=Comment)