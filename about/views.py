from django.shortcuts import render
from .models import About
# Create your views here.

def about(request):
    about = About.objects.get()
    context = {
        'about': about,
    }
    return render(request, 'about/about_page.html', context)
