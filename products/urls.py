from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name="detail"),
    path('json', views.products_json, name="products_json"),
    path('json_details/<int:product_id>', views.product_details_json, name="product_details_json")
]