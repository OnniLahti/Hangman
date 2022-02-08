import unittest


from main import name
from string_helper import is_name

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        self.assertTrue(is_name(name, ignore_case=True))
        self.assertTrue(is_name("Ville virtanen", ignore_case=True))
        self.assertTrue(is_name("ville virtanen", ignore_case=True))
        self.assertTrue(is_name("Ville Virtanen", ignore_case=False))
        self.assertTrue(is_name("ville virtanen", ignore_case=False))
        self.assertTrue(is_name("Ville virtanen", ignore_case=False))