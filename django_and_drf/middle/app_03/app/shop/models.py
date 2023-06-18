from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    """Category shops""" 

    transplations = TranslatedFields(
    name = models.CharField(max_length=200, help_text='Enter name of shop product'),
    slug = models.SlugField(max_length=200, unique=True)
    )

    class Meta:

        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    
class Product(TranslatableModel):
    translations = TranslatedFields(
    name = models.CharField(max_length=200, help_text='Enter product name '),
    slug = models.SlugField(max_length=200),
    description = models.TextField(blank=True, help_text='Enter description of product')
    )
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, 
                                on_delete=models.CASCADE, 
                                related_name='products')
    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
