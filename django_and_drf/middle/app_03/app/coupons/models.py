from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    """Coupon model"""

    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField(auto_now_add=True)
    valid_to = models.DateTimeField(auto_now=True)
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Процент скидки (от 0 до 100)",
        default=0,
        null=True,
    )
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.code
