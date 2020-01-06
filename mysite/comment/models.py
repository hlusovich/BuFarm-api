from django.db import models



class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey('user.User',on_delete=models.CASCADE,related_name="user_comments",null = True)
    product = models.ForeignKey('product.Product',on_delete=models.CASCADE,related_name="product_comments",null=True)

# Create your models here.
