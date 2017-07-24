import unittest
from flask_api.flask_api import app


class TestFlaskAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_uri(self):
        register = self.client.post('/register')
        self.assertEqual(register.status_code, 200)
