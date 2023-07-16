from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from restaurant.models import Menu
from restaurant.serializers import menuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Cheese Burger", price=5.99, inventory=10)
        self.menu2 = Menu.objects.create(title="Veggie Burger", price=4.99, inventory=5)
        self.menu3 = Menu.objects.create(title="Chicken Burger", price=6.99, inventory=8)

    def test_getall(self):
        response = self.client.get(reverse('restaurant:menu')) 
        menus = Menu.objects.all()
        serializer = menuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
