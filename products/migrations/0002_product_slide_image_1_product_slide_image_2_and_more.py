# Generated by Django 4.2.6 on 2023-10-14 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slide_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='mediaProduct/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='slide_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='mediaProduct/products'),
        ),
        migrations.AddField(
            model_name='product',
            name='slide_image_3',
            field=models.ImageField(blank=True, null=True, upload_to='mediaProduct/products'),
        ),
    ]