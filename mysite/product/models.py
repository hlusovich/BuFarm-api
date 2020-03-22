from django.db import models


class Product(models.Model):
    MILK_CHOICE = "milk"
    CHEESE_CHOICE = "cheese"
    SOUR_CREAME_CHOICE = "sour_creame"
    TYPE_CHOICES = (
        (MILK_CHOICE, "молоко"),
        (CHEESE_CHOICE,"сыр"),
        (SOUR_CREAME_CHOICE,"сметана"))

    AVAILABLE='available'
    UNAVAILABLE = 'unavailable'
    WILL_BE_SOON_AVAILABLE = 'available_soon'
    STATUS_CHOICES = (
        (AVAILABLE,'есть в наличии'),
        (UNAVAILABLE,'нет в наличии'),
        (WILL_BE_SOON_AVAILABLE,'скоро будет в наличии'),
    )

    KILOGRAMM_CHOICE='kilogramm'
    LITER_CHOICE="liter"
    PIECE_CHOICE='piece'
    UNIT_TYPE_CHOICES=(
        (LITER_CHOICE,'литр'),
        (PIECE_CHOICE,'штука'),
        (KILOGRAMM_CHOICE,'килограмм')
    )
    name = models.CharField(max_length=32)
    type = models.CharField(choices=TYPE_CHOICES, default=MILK_CHOICE,max_length=20)
    status = models.CharField(choices= STATUS_CHOICES,default=AVAILABLE,max_length=50)
    unit_type=models.CharField(choices=UNIT_TYPE_CHOICES,default=PIECE_CHOICE,max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2,default=0.00)
    info=models.TextField(default=True)


def product_image_directory_path(instance, filename):
    return f'product_{instance.product.id}/{filename}'


class ProductImage(models.Model):
    image = models.ImageField(upload_to=product_image_directory_path)
    product = models.ForeignKey('product.Product',on_delete=models.CASCADE,related_name='product_images')


class OrderedProduct(models.Model):
    order = models.ForeignKey('order.Order',on_delete=models.CASCADE,related_name="products", null=True)
    product = models.ForeignKey('product.Product',on_delete=models.CASCADE, related_name='ordered_products')
    count = models.IntegerField()
# Create your models here.
