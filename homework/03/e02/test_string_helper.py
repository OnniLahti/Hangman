import unittest

from main import name
from string_helper import is_name

class TestStringHelper(unittest.TestCase):
    def test_is_name(self):
        self.assertTrue(is_name(name))