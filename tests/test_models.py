from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Paneer", price=120.0, inventory=4)
        self.assertEqual(item.__str__(), "Paneer : 120.0")
