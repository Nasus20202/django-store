from django.urls import path

from . import views

app_name = "products"
urlpatterns = [
    path('', views.index_view, name='index'),
    path('<str:category_name>/', views.category_view, name='category')
]
