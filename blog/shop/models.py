from django.conf import settings
from django.db import models

STATUS_CHOICES = (("In Stock", "IN_STOCK"), ("Out Of Stock", "OUT_OF_STOCK"))

ORDER_BY_CHOICES = (
    ("price_asc", "Price Asc"),
    ("price_desc", "Price Desc"),
    ("max_count", "Max Count"),
    ("max_price", "Max Price"),
)


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(default="")
    image = models.ImageField(null=True, blank=True)
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, default="IN_STOCK"
    )


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE
    )
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.user} - {self.product} - {self.count}"
