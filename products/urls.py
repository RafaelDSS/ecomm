from django.urls import path
from products import views

urlpatterns = [
    path("list/", views.list_products, name="list"),
    path("create/", views.create_product, name="create"),
    path("delete/<int:product_id>", views.delete_product, name="delete"),
    path("update/<int:product_id>", views.update_product, name="update"),
]
