import unittest
import datetime

from main_prog.main_prog import return_today_date


class DummyTest(unittest.TestCase):
    def test_return_today_date(self):
        now = datetime.datetime.now()
        self.assertEqual(now.strftime('%d-%m-%Y'), return_today_date())
