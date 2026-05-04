from django.db import models
from core.common_model import BaseModel
# Create your models here.
class Product(BaseModel):
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, related_name='products'
        )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)


class ProductVariant(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='variants')

    sku = models.CharField(max_length=100, unique=True)

    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)

    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    stock = models.PositiveIntegerField(default=0)

    is_default = models.BooleanField(default=False)


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='images')

    image = models.ImageField(upload_to='products/')

    is_primary = models.BooleanField(default=False)

class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )

class ProductAttribute(BaseModel):
    name = models.CharField(max_length=100)  # e.g. "Material", "Brand"

class ProductAttributeValue(BaseModel):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='attributes')

    attribute = models.ForeignKey(
        ProductAttribute, on_delete=models.CASCADE)

    value = models.CharField(max_length=255)




# relationg these models together, we have:
# #```
# Product
#    ├── Variants (size, color, stock)
#    ├── Images
#    ├── Attributes (material, brand, etc)
#    └── Category

# #```