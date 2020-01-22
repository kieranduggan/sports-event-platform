import unittest
import sys
from mock import Mock, patch

sys.path.append(sys.path[0] + "/..")
import app.app as app

class TestApp(unittest.TestCase):

    @patch('app.EventHandler')
    def test_send_response(self, handler):
        with patch