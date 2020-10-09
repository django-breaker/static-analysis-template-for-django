from django.conf import settings
from django.test import SimpleTestCase
from rest_framework import status
from rest_framework.test import APIClient


class MocksViewIndexTest(SimpleTestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_view(self):
        response = self.client.get('/mocks', format='json').json()

        self.assertEqual(response['timezone'], settings.TIME_ZONE)
        self.assertIsInstance(response['timestamp'], int)
        self.assertIsInstance(response['formatted_datetime'], str)

    def test_create_view(self):
        response = self.client.post(
            '/mocks', {'timestamp': 1602008716170, 'timezone': 'Asia/Seoul'}, format='json'
        ).json()

        self.assertEqual(response['timezone'], 'Asia/Seoul')
        self.assertEqual(response['timestamp'], 1602008716170)
        self.assertEqual(response['formatted_datetime'], '2020-10-07 03:25:16 +09:00')

        response = self.client.post(
            '/mocks', {'timestamp': 1602008716170, 'timezone': 'America/New York'}, format='json'
        ).json()

        self.assertEqual(response['timezone'], 'America/New York')
        self.assertEqual(response['timestamp'], 1602008716170)
        self.assertEqual(response['formatted_datetime'], '2020-10-06 14:25:16 -04:00')

        response = self.client.post(
            '/mocks', {'timestamp': 1602008749885, 'timezone': 'Asia/Riyadh'}, format='json'
        ).json()

        self.assertEqual(response['timezone'], 'Asia/Riyadh')
        self.assertEqual(response['timestamp'], 1602008749885)
        self.assertEqual(response['formatted_datetime'], '2020-10-06 21:25:49 +03:00')

        # Invalid timezone
        response = self.client.post(
            '/mocks', {'timestamp': 1602008716170, 'timezone': 'INVALIDTIMEZONE'}, format='json'
        ).json()

        self.assertIn('non_field_errors', response.keys())
        self.assertIsInstance(response['non_field_errors'], list)
        self.assertEqual(len(response['non_field_errors']), 1)

        # Invalid timestamp
        response = self.client.post(
            '/mocks', {'timestamp': 160200871617090293090, 'timezone': 'Asia/Seoul'}, format='json'
        ).json()
        self.assertIsInstance(response['non_field_errors'], list)
        self.assertEqual(len(response['non_field_errors']), 1)

    def test_update_view(self):
        _id = 25
        response = self.client.put(f'/mocks/{_id}', format='json').json()

        self.assertEqual(response['_id'], f'{_id}')

    def test_destroy_view(self):
        _id = 25
        status_code = self.client.delete(f'/mocks/{_id}', format='json').status_code

        self.assertEqual(status_code, status.HTTP_423_LOCKED)

    def test_hello_action_view(self):
        response = self.client.get('/mocks/hello', format='json').json()

        self.assertEqual(response.get('hello'), 'hello')
        self.assertEqual(response['hello'], 'hello')

    def test_bye_action_view(self):
        _id = 25
        response = self.client.delete(f'/mocks/{_id}/bye', format='json').json()

        self.assertEqual(response['_id'], f'{_id}')
