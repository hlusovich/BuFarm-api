# Generated by Django 2.2.6 on 2020-03-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_address_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='flat',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
