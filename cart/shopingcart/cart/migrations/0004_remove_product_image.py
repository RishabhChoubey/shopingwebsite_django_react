# Generated by Django 3.0.2 on 2020-04-14 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
