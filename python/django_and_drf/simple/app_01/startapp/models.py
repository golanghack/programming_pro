from django.db import models

class AppDb(models.Model):

    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание товара')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Rubric')
    class Meta:

        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявления'
        ordering = ['-published']


class Rubric(models.Model):

    name = models.CharField(max_length=20, db_index=True, verbose_name='Title')
    def __str__(self) -> str:
        return self.name
    class Meta:

        verbose_name_plural = 'Rubric'
        verbose_name = 'Rubric'
        ordering = ['name']
        
    
