# Generated by Django 4.2.6 on 2023-10-14 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField()),
                ('description', models.CharField(max_length=150)),
                ('order', models.BooleanField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('featured', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='mediaProduct/products')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='mediaProduct/products')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='mediaProduct/products')),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='mediaProduct/products')),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='mediaProduct/products')),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='mediaProduct/products')),
                ('featured', models.BooleanField(default=False)),
                ('recent_product', models.BooleanField(default=False)),
                ('recent_remark', models.CharField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
            ],
        ),
    ]
