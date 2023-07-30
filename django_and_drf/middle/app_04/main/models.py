from django.db import models
import typing

from django.contrib.auth.models import AbstractUser

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

        