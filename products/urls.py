from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    path('', views.index_view, name='index'),
    path('product/<str:product_name>/', views.product_view, name='product'),
    path('<str:category_name>/', views.category_view, name='category'),
    path('<str:category_name>/<str:subcategory_name>/', views.subcategory_view, name='subcategory'),
]
