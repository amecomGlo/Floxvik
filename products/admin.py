from django.contrib import admin
from .models import Category, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'featured']
    prepopulated_fields = {'slug':('title',)}
    list_editable = ['featured',]

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    
    
admin.site.register(Product, ProductAdmin)