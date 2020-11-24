from django.db import models


def category_list_fun(order="name"):
    return Category.objects.all().order_by(order)


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

    def category_list(self, order="name"):
        return Category.objects.all().order_by(order)

    name = models.CharField(max_length=256, default='')
    shortName = models.CharField(max_length=32, default='')


class Subcategory(models.Model):
    def __str__(self):
        return self.name

    def product_list(self, order='name'):
        return self.product_set.all().order_by(order)

    name = models.CharField(max_length=256)
    shortName = models.CharField(max_length=32, default='')
    tags = models.CharField(max_length=1024, default='')
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
    about = models.CharField(max_length=4096, default='')
    photo = models.CharField(max_length=256, default='')

    def Subcategory(self):
        return self.subcategory

    def Category(self):
        return self.Subcategory().category
