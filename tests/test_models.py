from django.test import TestCase
from restaurant.models import Menu, Booking


# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="Cheese Burger", price=5.99, inventory=10)
        self.assertEqual(str(item), "Cheese Burger : $5.99")


class BookingItemTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(
            name="John", no_of_guests=5, booking_date="2021-10-10"
        )
        self.assertEqual(str(item), "John")
