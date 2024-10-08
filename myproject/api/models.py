from django.db import models

# Create your models here.
class Product(models.Models):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name