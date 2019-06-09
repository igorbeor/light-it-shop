from django.db import models


class Category(models.Model):
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)


class Item(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=255)
    image_url = models.URLField()
