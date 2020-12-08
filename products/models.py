from django.db import models
from django.utils import timezone


def category_list_fun(order="name"):
    return Category.objects.all().order_by(order)


class Category(models.Model):
    def __str__(self):
        return self.name

    def subcategory_list(self, order='name'):
        return self.subcategory_set.all().order_by(order)

    def product_list(self, order='name'):
        product_list = []
        for subcategory in self.subcategory_list():
            for product in subcategory.product_list(order):
                product_list.append(product)
        if order == 'name':
            product_list.sort(key=lambda x: x.name, reverse=True)
        elif order == '-name':
            product_list.sort(key=lambda x: x.name, reverse=False)
        elif order == '-price':
            product_list.sort(key=lambda x: x.price, reverse=True)
        elif order == 'price':
            product_list.sort(key=lambda x: x.price, reverse=False)
        else:
            product_list.sort(key=lambda x: x.times_bought, reverse=True)

        for i in product_list:
            print(i, i.times_bought)
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
    tags = models.TextField(max_length=1024, default='')
    about = models.TextField(max_length=10240, default='')
    shortAbout = models.TextField(max_length=512, default='')
    photo = models.CharField(max_length=256, default='')
    rating = models.IntegerField(default=0)
    votes = models.IntegerField(default=0)

    def Subcategory(self):
        return self.subcategory

    def Category(self):
        return self.Subcategory().category

    def Price_divided(self):
        return self.price/100

    def Rating(self):
        if self.votes>0:
            return format(self.rating/self.votes, '.2f')
        else:
            return 'Brak'


class Order(models.Model):
    def __str__(self):
        return self.orderId

    orderId = models.IntegerField(default=0)
    name = models.CharField(max_length=64, default='')
    surname = models.CharField(max_length=64, default='')
    email = models.CharField(max_length=128, default='')
    address = models.CharField(max_length=64, default='')
    date = models.DateTimeField(default=timezone.now())
    cost = models.IntegerField(default=0)
    products = models.TextField(default='')
    payment = models.IntegerField(default=0)
    delivery = models.IntegerField(default=0)




