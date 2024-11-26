import unittest
from app import create_app, mongo
from flask import json

class TestUserRoutes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
        cls.db = mongo.db.users

        # Clear the users collection before tests
        cls.db.drop()

    def test_create_user(self):
        payload = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'password': 'password123'
        }
        response = self.client.post('/users', json=payload)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'John Doe')
        self.assertEqual(data['email'], 'john.doe@example.com')

    def test_get_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIsInstance(data, list)

    def test_get_user_by_id(self):
        user = self.db.find_one({'email': 'john.doe@example.com'})
        response = self.client.get(f'/users/{user["_id"]}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'John Doe')

    def test_update_user(self):
        user = self.db.find_one({'email': 'john.doe@example.com'})
        payload = {
            'name': 'John Updated',
            'email': 'john.doe@example.com',
            'password': 'newpassword123'
        }
        response = self.client.put(f'/users/{user["_id"]}', json=payload)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'John Updated')

    def test_delete_user(self):
        user = self.db.find_one({'email': 'john.doe@example.com'})
        response = self.client.delete(f'/users/{user["_id"]}')
        self.assertEqual(response.status_code, 200)
        user = self.db.find_one({'email': 'john.doe@example.com'})
        self.assertIsNone(user)

    @classmethod
    def tearDownClass(cls):
        # Clean up by dropping the users collection after tests
        cls.db.drop()

if __name__ == '__main__':
    unittest.main()
