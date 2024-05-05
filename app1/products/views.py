from django.shortcuts import render
from .models import Category, Products, products


# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request, 'index.html', context=context )

