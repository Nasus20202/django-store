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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product)
admin.site.register(Order)
