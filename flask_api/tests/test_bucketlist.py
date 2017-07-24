import unittest
from flask_api.models.bucketslist.bucketlist import Bucketlist


class TestUser(unittest.TestCase):
    def test_is_user(self):
        """
        This method test if the user created is class Bucketlist
        """
        new_bucketlist = Bucketlist('test')
        self.assertIsInstance(new_bucketlist, Bucketlist)

if __name__ == '__main__':
    unittest.main()
