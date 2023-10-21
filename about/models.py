from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class About(models.Model):
    description = models.CharField(max_length=250)
    mission_statement = models.CharField(max_length=250, blank=True, null=True)
    vision_statement = models.CharField(max_length=250, blank=True, null=True)
    about_image = models.ImageField(upload_to='mediaProduct/products', null=True, blank=True)
    video = EmbedVideoField(blank=True)
    slide_image_1 = models.ImageField(upload_to='mediaProduct/products', null=True, blank=True)
    slide_image_2 = models.ImageField(upload_to='mediaProduct/products', null=True, blank=True)
    slide_image_3 = models.ImageField(upload_to='mediaProduct/products', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.description
    