from django.db import models

# Create your models here.
class ProductModel(models.Model):
    Segment = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Product = models.CharField(max_length=100)
    Units = models.IntegerField()
    Sales = models.IntegerField()
    Date_sold = models.CharField(max_length=100)

    def __str__(self):
        return self.Product