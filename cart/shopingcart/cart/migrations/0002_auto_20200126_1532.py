# Generated by Django 2.2.8 on 2020-01-26 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0, max_length=15),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(default='a', max_length=15),
        ),
    ]
