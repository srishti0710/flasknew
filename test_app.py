import unittest
from app import app

class AppTests(unittest.TestCase):

    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Test the home route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"message": "Welcome to the Flask App!"})

if __name__ == '__main__':
    unittest.main()