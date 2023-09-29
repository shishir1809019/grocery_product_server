from django.db import models

class ProductData(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    photo_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
