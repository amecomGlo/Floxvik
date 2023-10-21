from django.shortcuts import get_object_or_404, render
from about.models import About
from products.models import Category, Product


def home(request):
    about = About.objects.get(is_active=True)
    print(about)
    categories = Category.objects.all()
    recent = Product.objects.order_by('-featured').all()[:4]
    
    context = {
        'categories': categories,
        'recent': recent,
        'about': about,
    }
    return render(request, 'products/home.html', context)


def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    related_product = Product.objects.filter(category=product.category).exclude(slug=product.slug)
    context = {
        'product': product,
        'related_product': related_product,
    }
    return render(request, 'products/detail.html', context)



def product_lists(request):
    categories = Category.objects.all()
    
    context = {
        'categories': categories,

    }
    return render(request, 'products/product_lists.html', context)