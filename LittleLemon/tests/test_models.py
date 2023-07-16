from django.test import TestCase
from restaurant.models import Menu

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Cheese Burger", price=5.99, inventory=10)
        self.assertEqual(str(item), "Cheese Burger : $5.99")