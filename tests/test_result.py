from os.path import dirname, join
import unittest

from YouTubeAPI import Result

THIS_DIR = dirname(__file__)


class TestResult(unittest.TestCase):

    def setUp(self):
        with open(join(THIS_DIR, "example_raw.json"), "r") as f:
            self.r1 = Result(f.read())
        super(TestResult, self).setUp()

    def tearDown(self):
        super(TestResult, self).tearDown()

    def test_title(self):
        with open(join(THIS_DIR, "expected_titles.txt"), "r") as f:
            expected = f.read().strip()
        actual = self.r1.render()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

