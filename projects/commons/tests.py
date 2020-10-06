from django.conf import settings
from django.test import SimpleTestCase

from commons.utils import get_current_server_time_info, get_local_time_info

class CommonsUtilTest(SimpleTestCase):
    def test_get_current_server_time_info(self):
        '''
        {
            "formatted_datetime": "2020-10-06 17:57:37 +00:00",
            "timestamp": 1602007057696,
            "timezone": "UTC"
        }
        '''

        result_1 = get_current_server_time_info()
        result_2 = get_current_server_time_info()
        result_3 = get_current_server_time_info()

        self.assertIsInstance(result_1['formatted_datetime'], str)
        self.assertIsInstance(result_1['timestamp'], int)
        self.assertEqual(result_1['timezone'], settings.TIME_ZONE)

        self.assertIsInstance(result_2['formatted_datetime'], str)
        self.assertIsInstance(result_2['timestamp'], int)
        self.assertEqual(result_2['timezone'], settings.TIME_ZONE)

        self.assertIsInstance(result_3['formatted_datetime'], str)
        self.assertIsInstance(result_3['timestamp'], int)
        self.assertEqual(result_3['timezone'], settings.TIME_ZONE)

    def test_get_local_time_info(self):
        '''
        {
            "formatted_datetime": "2020-10-06 17:57:37 +00:00",
            "timestamp": 1602008749885,
            "timezone": "Asia/Seoul"
        }
        '''

        data_1 = {'timestamp': 1602008716170, 'timezone': 'Asia/Seoul'}
        data_2 = {'timestamp': 1602008716170, 'timezone': 'America/New York'}
        data_3 = {'timestamp': 1602008749885, 'timezone': 'Asia/Riyadh'}

        result_1 = get_local_time_info(**data_1)
        result_2 = get_local_time_info(**data_2)
        result_3 = get_local_time_info(**data_3)

        self.assertEqual(result_1['timezone'], data_1['timezone'])
        self.assertEqual(result_1['timestamp'], data_1['timestamp'])
        self.assertEqual(result_1['formatted_datetime'], '2020-10-07 03:25:16 +09:00')

        self.assertEqual(result_2['timezone'], data_2['timezone'])
        self.assertEqual(result_2['timestamp'], data_2['timestamp'])
        self.assertEqual(result_2['formatted_datetime'], '2020-10-06 14:25:16 -04:00')

        self.assertEqual(result_3['timezone'], data_3['timezone'])
        self.assertEqual(result_3['timestamp'], data_3['timestamp'])
        self.assertEqual(result_3['formatted_datetime'], '2020-10-06 21:25:49 +03:00')
