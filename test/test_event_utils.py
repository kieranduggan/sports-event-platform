import unittest
import sys
from mock import Mock, patch, MagicMock

sys.path.append(sys.path[0] + "/..")
import app.event_utils as utils
import test_helper as helper


class TestEventUtils(unittest.TestCase):

    def test_get_event_by_name(self):
        redis_db = Mock()
        redis_db.keys.return_value = ["test"]
        redis_db.mget.return_value = ["abc"]
        with patch('app.event_utils.json.loads') as mock_loads:
            mock_loads.return_value = helper.mock_event_1
            event = utils.get_event_by_name("cork vs galway", redis_db)
            self.assertEqual(event, helper.mock_event_1)

    def test_get_sorted_sports_events(self):
        redis_db = Mock()
        redis_db.keys.return_value = ["test"]
        redis_db.mget.return_value = ["abc"]
        with patch('app.event_utils.json.loads') as mock_loads:
            with patch('app.event_utils.create_event_details') as mock_event_details:
                mock_loads.return_value = helper.mock_event_1
                mock_event_details.return_value = helper.mock_event_details_1
                sorted_details = utils.get_sorted_sports_events("hurling", "startTime", redis_db)
                self.assertEqual(sorted_details[0], helper.mock_event_details_1)

    def test_create_event_details(self):
        event = utils.create_event_details(helper.mock_event_1)
        expected_result = {
            "id": 1,
            "url": "http://example.com/api/match/1",
            "name": "Cork vs Galway",
            "startTime": "2020-04-19 15:35:00"
        }
        self.assertEqual(event, expected_result)

    def test_add_event_url(self):
        with patch('app.event_utils.generate_event_url') as mock_generate:
            mock_generate.return_value = 'http://abc.com/api/match/1'
            mock_event = {"id": 1}
            utils.add_event_url(mock_event)
            self.assertEqual(mock_event["url"], 'http://abc.com/api/match/1')

    def test_generate_url(self):
        expected_string = f'http://localhost:8080/api/match/1'
        self.assertEqual(utils.generate_event_url(1), expected_string)


if __name__ == '__main__':
    unittest.main()
