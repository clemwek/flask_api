import unittest
from flask_api.models.items.item import Item


class TestUser(unittest.TestCase):
    def test_is_user(self):
        """
        This method test if the user created is class Items
        """
        new_item = Item('bucket_id', 'test', 'description', 'date')
        self.assertIsInstance(new_item, Item)

if __name__ == '__main__':
    unittest.main()
