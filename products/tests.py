from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductStrTestCase(TestCase):
    def test_str_should_return_name(self):
        product = Product.objects.create(
            name="Product test", description="Description test", price=10.90
        )
        assert str(product) == "Name test"
