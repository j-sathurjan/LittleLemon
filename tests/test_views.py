from django.test import TestCase, Client
from django.http import response
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setup(self):
        self.client=Client()
        self.menu1=Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.menu2=Menu.objects.create(title="cake", price=50, inventory=20)
        self.menu3=Menu.objects.create(title="bun", price=40, inventory=50)
        
    def test_getall(self):
        menus=Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)