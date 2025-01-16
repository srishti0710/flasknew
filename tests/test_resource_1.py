import unittest
from resource_1 import resource_bp
from flask import Flask
class ResourceTests(unittest.TestCase):

    def setUp(self):
        # Create a test app and register the blueprint
        self.app = Flask(__name__)
        self.app.register_blueprint(resource_bp)
        self.client = self.app.test_client()
        self.app.testing = True

    def test_get_resource(self):
        # Test the GET resource route
        response = self.client.get('/api/resource')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"resource": "This is a sample resource."})


if __name__ == '__main__':
    unittest.main()