# Generated by Django 5.0.2 on 2024-02-19 02:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0002_cartitem_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="img",
            field=models.ImageField(default="4:35 p.m.", upload_to="Gallery"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="cartitem",
            name="img",
            field=models.ImageField(default="gallery", upload_to="Gallery"),
            preserve_default=False,
        ),
    ]
