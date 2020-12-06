from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext
from .models import *


def index_view(request):
    category_list = Category.objects.all().order_by('name')
    context = {'category_list': category_list}
    return render(request, 'products/index.html', context)


def category_view(request, category_name):
    category = get_object_or_404(Category, shortName__iexact=category_name)
    try:
        sort = request.GET['sort']
        if sort not in {'name', '-name', 'price', '-price', '-times_bought'}:
            sort = '-times_bought'
    except:
        sort = '-times_bought'
    context = {'category': category, 'sort': sort}
    return render(request, 'products/category.html', context)


def subcategory_view(request, category_name, subcategory_name):
    category = get_object_or_404(Category, shortName__iexact=category_name)
    subcategory = get_object_or_404(Subcategory, shortName__iexact=subcategory_name)
    try:
        sort = request.GET['sort']
        if sort not in {'name', '-name', 'price', '-price', '-times_bought'}:
            sort = '-times_bought'
    except:
        sort = '-times_bought'
    context = {'category': category, 'subcategory': subcategory, 'sort': sort}
    return render(request, 'products/subcategory.html', context)


def product_view(request, product_name):
    product = get_object_or_404(Product, shortName__iexact=product_name)
    context = {'product': product, }
    return render(request, 'products/product.html', context)


def search(request):
    category_list = Category.objects.all().order_by('name')
    try:
        value = request.GET['value']
        found = Product.objects.filter(Q(name__contains=value) | Q(brand__contains=value))

    except:
        value = 'Undefined'
        found = []

    context = {'category_list': category_list, 'value': value, 'found': found}
    return render(request, 'products/search.html', context)


def add_to_cart(request, product_name):
    product = get_object_or_404(Product, shortName__iexact=product_name)
    cart = request.session.get('cart', {})
    if cart.__contains__(product_name):
        cart[product_name] += 1
    else:
        cart[product_name] = 1
    request.session['cart'] = cart
    return HttpResponseRedirect(reverse('products:cart'))


def cart(request):
    cartData = request.session.get('cart', {})
    category_list = Category.objects.all().order_by('name')
    cart = {}
    for i in cartData:
        if cart.__contains__(i):
            cart[i] += cartData[i]
        else:
            cart[i] = cartData[i]
    context = {'category_list': category_list, 'cart': cart}
    return render(request, 'products/cart.html', context)


def clear(request):
    request.session['cart'] = {}
    return HttpResponseRedirect(reverse('products:index'))


def remove(request, product_name):
    cartData = request.session.get('cart', {})
    cart = {}
    for i in cartData:
        if cart.__contains__(i):
            cart[i] += cartData[i]
        else:
            cart[i] = cartData[i]
    cart.pop(product_name)
    request.session['cart'] = cart
    return HttpResponseRedirect(reverse('products:cart'))


def change(request, product_name, value):
    value = int(value)
    cartData = request.session.get('cart', {})
    cart = {}
    for i in cartData:
        if cart.__contains__(i):
            cart[i] += cartData[i]
        else:
            cart[i] = cartData[i]
    cart[product_name] += value;
    if cart[product_name] <= 0:
        cart.pop(product_name)
    request.session['cart'] = cart
    return HttpResponseRedirect(reverse('products:cart'))
