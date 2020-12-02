from django import template

register = template.Library()


@register.simple_tag
def products(value, arg):
    return value.product_list(arg)
