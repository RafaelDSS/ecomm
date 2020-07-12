from django.test import TestCase
from .models import Product, Category

# Create your tests here.


class ProductStrTestCase(TestCase):
    def test_str_should_return_name(self):
        expect = "Product test"

        category = Category.objects.create(
            name="Category test", description="Description test")
        product = Product.objects.create(
            name="Product test", description="Description test", price=10.90, category=category
        )
        result = Product.objects.filter(category=category.id).first()

        assert str(result) == expect
