from django.contrib import admin
from products.models import *


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryInline]


class SubcategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'stock', 'price')
    search_fields = ['name', 'brand', 'shortName']


class OrderAdmin(admin.ModelAdmin):
    list_filter = ['date']
    search_fields = ['orderId', 'name', 'surname', 'email']
    list_display = ('orderId', 'email' ,'cost')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
