# Generated by Django 5.0.2 on 2024-02-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshopapp', '0002_rename_customer_order_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='products/'),
        ),
    ]
