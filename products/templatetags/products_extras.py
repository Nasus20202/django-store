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
