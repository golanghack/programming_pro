from django.db import models


class AppDb(models.Model):

    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание товара')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')


    class Meta:

        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявления'
        ordering = ['-published']
