from django.db import models


class Category(models.Model):
    def __str__(self):
        return self.name

    def subcategory_list(self, order='name'):
        return self.subcategory_set.all().order_by(order)

    def product_list(self, order='name'):
        product_list = []
        for subcategory in self.subcategory_list(order):
            for product in subcategory.product_list(order):
                product_list.append(product)
        return product_list

    name = models.CharField(max_length=256, default='')
    shortName = models.CharField(max_length=32, default='')


class Subcategory(models.Model):
    def __str__(self):
        return self.name

    def product_list(self, order='name'):
        return self.product_set.all().order_by(order)

    name = models.CharField(max_length=256)
    shortName = models.CharField(max_length=32, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Product(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=256, default='')
    shortName = models.CharField(max_length=32, default='')
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    times_bought = models.IntegerField(default=0)
    recentViews = models.IntegerField(default=0)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    brand = models.CharField(max_length=128, default='')
    tags = models.CharField(max_length=1024, default='')
