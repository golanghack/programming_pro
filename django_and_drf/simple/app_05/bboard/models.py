from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Cost')
    content = models.TextField(null=True, blank=True, verbose_name='content')
    price = models.FloatField(null=True, blank=True, verbose_name='price')
    published = models.DateTimeField(auto_now_add=True, 
                                    db_index=True, verbose_name='Published')

    class Meta:
        verbose_name_plural = 'Boards'
        verbose_name = 'Board'
        ordering = ['-published']