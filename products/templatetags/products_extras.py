from django import template
from ..models import *

register = template.Library()


@register.simple_tag
def products(value, arg):
    return value.product_list(arg)


@register.simple_tag
def product_by_shortName(value):
    product = Product.objects.get(shortName__iexact=value)
    return product


@register.filter
def item(value, arg):
    try:
        return value[arg]
    except:
        return None


@register.simple_tag
def multiply(a, b):
    result = a*b
    result = str(result)
    result2 = ''
    for i in result:
        if i == '.':
            result2 += ','
        else:
            result2 += i
    return result2


@register.simple_tag
def price_sum(cart):
    sum = 0
    for name in cart:
        product = Product.objects.get(shortName__iexact=name)
        sum += product.price*cart[product.shortName]
    sum = sum/100
    sum = str(sum)
    result = ''
    for i in sum:
        if i == '.':
            result += ','
        else:
            result += i
    return result


@register.simple_tag
def isRated(request, product_name):
    try:
        if request.session['rated:'+product_name]:
            return True
        else:
            return False
    except:
        return False