# Generated by Django 3.1.4 on 2020-12-19 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_order_product'),
        ('products', '0007_remove_product_sold_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sold_to', to='orders.order'),
        ),
    ]
