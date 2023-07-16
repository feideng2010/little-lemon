from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from restaurant.models import Menu, Booking
from restaurant.serializers import menuSerializer, bookingSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(
            title="Cheese Burger", price=5.99, inventory=10
        )
        self.menu2 = Menu.objects.create(title="Veggie Burger", price=4.99, inventory=5)
        self.menu3 = Menu.objects.create(
            title="Chicken Burger", price=6.99, inventory=8
        )

    def test_getall(self):
        response = self.client.get(reverse("restaurant:menu"))
        menus = Menu.objects.all()
        serializer = menuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookingViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user("TestUser", "test@little.com", "test@123")
        self.client.login(username="TestUser", password="test@123")

        self.booking1 = Booking.objects.create(
            name="John", no_of_guests=5, booking_date="2021-10-10"
        )
        self.booking2 = Booking.objects.create(
            name="Jane", no_of_guests=2, booking_date="2021-10-11"
        )
        self.booking3 = Booking.objects.create(
            name="Jack", no_of_guests=3, booking_date="2021-10-12"
        )

    def test_getall(self):
        response = self.client.get(reverse("table-list"))
        bookings = Booking.objects.all()
        serializer = bookingSerializer(bookings, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def tearDown(self):
        self.client.logout()
        self.user.delete()
