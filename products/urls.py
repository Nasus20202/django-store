from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    path('', views.index_view, name='index'),
    path('search/', views.search, name='search'),
    path('cart/', views.cart, name='cart'),
    path('clear/', views.clear, name='clear_cart'),
    path('order/', views.order, name='order'),
    path('rate/<str:product_name>/<int:rate>', views.rate, name='rate'),
    path('remove/<str:product_name>/', views.remove, name='remove_from_cart'),
    path('change/<str:product_name>/<str:value>', views.change, name='change_cart'),
    path('add/<str:product_name>/', views.add_to_cart, name='add_to_cart'),
    path('product/<str:product_name>/', views.product_view, name='product'),
    path('<str:category_name>/', views.category_view, name='category'),
    path('<str:category_name>/<str:subcategory_name>/', views.subcategory_view, name='subcategory'),
]
