from json import JSONDecoder
from os.path import dirname, join
import unittest

from YouTubeAPI import Request

THIS_DIR = dirname(__file__)


class TestResult(unittest.TestCase):

    def setUp(self):
        super(TestResult, self).setUp()

    def tearDown(self):
        super(TestResult, self).tearDown()

    def test_most_viewed(self):
        expected="http://gdata.youtube.com/feeds/api/standardfeeds/most_viewed?alt=json"
        actual = Request().url
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

