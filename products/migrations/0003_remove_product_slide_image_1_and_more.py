# Generated by Django 4.2.6 on 2023-10-14 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_slide_image_1_product_slide_image_2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slide_image_1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slide_image_2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slide_image_3',
        ),
    ]
