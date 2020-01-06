# Generated by Django 2.2.6 on 2019-11-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('building', models.CharField(max_length=10)),
                ('flat', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
