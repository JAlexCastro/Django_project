# Generated by Django 5.0 on 2023-12-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productApp", "0002_alter_product_img_producto"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="img_producto",
            field=models.ImageField(null=True, upload_to="products"),
        ),
    ]
