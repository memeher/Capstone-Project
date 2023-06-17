from django.test import TestCase
from restaurant import views
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
import json

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(menu_id=3, title="Paneer roll", price=12.50, inventory=5)
        Menu.objects.create(menu_id=5, title="Burger", price=8.99, inventory=10)
        Menu.objects.create(menu_id=7, title="Salad", price=6.75, inventory=8)

    def test_getall(self):
        client = APIClient()
        response = client.get('/menus/', format='json', **{'HTTP_ACCEPT': 'application/json'})
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response_data, serializer.data)

