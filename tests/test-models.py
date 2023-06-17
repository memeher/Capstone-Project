from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(
            menu_id=2, title="Tacos", price=14.00, inventory=3
        )
        self.assertEqual(item, "Tacos : 14.00")