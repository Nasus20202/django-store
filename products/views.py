from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import *


def index_view(request):
    category_list = Category.objects.all().order_by('name')
    context = {'category_list': category_list}
    return render(request, 'products/index.html', context)


def category_view(request, category_name):
    category = get_object_or_404(Category, shortName__iexact=category_name)
    category_list = Category.objects.all().order_by('name')
    subcategory_list = category.subcategory_list()
    context = {'category_list': category_list, 'subcategory_list': subcategory_list}
    return render(request, 'products/category.html', context)


def subcategory_view(request, category_name, subcategory_name):
    category = get_object_or_404(Category, shortName__iexact=category_name)
    subcategory = get_object_or_404(Subcategory, shortName__iexact=subcategory_name)
    category_list = Category.objects.all().order_by('name')
    subcategory_list = category.subcategory_list()
    product_list = subcategory.product_list()
    context = {'category_list': category_list, 'subcategory_list': subcategory_list, 'product_list': product_list}
    return render(request, 'products/subcategory.html', context)
