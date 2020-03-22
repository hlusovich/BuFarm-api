# Generated by Django 2.2.6 on 2020-01-29 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderedproduct',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='order.Order'),
        ),
    ]
