from django.db import models
from slugify import slugify
from discount.models import Discount


class Attribute(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False, blank=True)

class ProductGallery(models.Model):
    alt = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/product')


class Product(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/product', null=True, blank=True)
    gallery = models.ManyToManyField(ProductGallery, null=True, blank=True, related_name="productGallery")
    description = models.TextField(db_index=True)
    price = models.FloatField()
    discount = models.ForeignKey(
        Discount, on_delete=models.CASCADE, null=True, blank=True, related_name="products")
    attribute = models.ManyToManyField(
        Attribute, null=True, blank=True, related_name="products")
    count = models.IntegerField()
    slug = models.SlugField(null=False, db_index=True,
                            blank=True, max_length=200, unique=True)
    is_active = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

