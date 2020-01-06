from django.db import models


class Order(models.Model):
    IN_PROGRESS_CHOICE='in_progress'
    CLOSED_CHOICE = 'closed'
    CANCELED_CHOICE = 'canceled'
    STATUS_CHOICES = (
        (IN_PROGRESS_CHOICE,"в обработке"),
        (CLOSED_CHOICE,"завершен"),
        (CANCELED_CHOICE,"отменен")
    )
    user = models.ForeignKey('user.User',on_delete=models.CASCADE,related_name="user_orders",null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES,default=IN_PROGRESS_CHOICE,max_length=50)