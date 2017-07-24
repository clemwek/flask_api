import unittest
from flask_api.models.users.user import User


class TestUser(unittest.TestCase):
    def test_is_user(self):
        """
        This method test if the user created is class user
        """
        new_user = User('test', 'test', 'test@test.com', 'test')
        self.assertIsInstance(new_user, User)

if __name__ == '__main__':
    unittest.main()
