from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *


def index_view(request):
    category_list = Category.objects.all().order_by('name')
    context = {'category_list': category_list}
    return render(request, 'products/index.html', context)


def category_view(request, category_name):
    category = get_object_or_404(Category, shortName__iexact=category_name)
    context = {'category': category, }
    return render(request, 'products/category.html', context)


def subcategory_view(request, category_name, subcategory_name):
    category = get_object_or_404(Category, shortName__iexact=category_name)
    subcategory = get_object_or_404(Subcategory, shortName__iexact=subcategory_name)
    context = {'category': category, 'subcategory': subcategory, }
    return render(request, 'products/subcategory.html', context)


def product_view(request, product_name):
    product = get_object_or_404(Product, shortName__iexact=product_name)
    context = {'product': product, }
    return render(request, 'products/product.html', context)


