# Generated by Django 3.2.6 on 2021-10-04 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_cost_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('In Stock', 'IN_STOCK'), ('Out Of Stock', 'OUT_OF_STOCK')], default='IN_STOCK', max_length=100),
        ),
    ]