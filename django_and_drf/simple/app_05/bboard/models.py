from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Cost')
    content = models.TextField(null=True, blank=True, verbose_name='content')
    price = models.FloatField(null=True, blank=True, verbose_name='price')
    published = models.DateTimeField(auto_now_add=True, 
                                    db_index=True, verbose_name='Published')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, 
                                                    verbose_name='Rubric')

    class Meta:
        verbose_name_plural = 'Boards'
        verbose_name = 'Board'
        ordering = ['-published']

class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True, verbose_name='Rubric')

    class Meta:
        verbose_name_plural = 'Rubrics'
        verbose_name = 'Rubric'
        ordering = ['name']
