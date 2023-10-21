from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    description = models.CharField(max_length=150)
    # image = models.ImageField(upload_to='mediaProduct/cat')
    order = models.BooleanField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-updated']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


      
class Product(models.Model):


    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True)
    category = models.ForeignKey(Category,related_name="products", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='mediaProduct/products', null=True, blank=True)
    image_1 = models.ImageField(upload_to='mediaProduct/products', null=True, blank=True)
    image_2 = models.ImageField(upload_to='mediaProduct/products', null=True, blank=True)
    image_3 = models.ImageField(upload_to='mediaProduct/products', null=True, blank=True)
    image_4 = models.ImageField(upload_to='mediaProduct/products', null=True, blank=True)
    image_5 = models.ImageField(upload_to='mediaProduct/products', null=True, blank=True)
    featured = models.BooleanField(default=False)
    recent_product = models.BooleanField(default=False)
    recent_remark = models.CharField(max_length=255, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug":self.slug})


def save_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    obj = Product.objects.filter(slug=slug)
    exists = obj.exists()
    if exists:
        new_slug = "%s/%s"%(slug, obj.first().id)
        return save_slug(instance, new_slug=new_slug)
    return slug

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug =  save_slug(instance)  

pre_save.connect(product_pre_save_receiver, sender=Product)

   