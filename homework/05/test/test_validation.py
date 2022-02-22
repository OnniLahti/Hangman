import unittest

from util.validation import is_date
# from util.validation import is_email
# from util.validation import is_personal_id

class TestValidation(unittest.TestCase):
    def test_is_date(self):
        self.assertTrue(is_date("2022-10-10"))
        self.assertTrue(is_date("0-10-10"))
        self.assertTrue(is_date("2022-0-10"))
        self.assertTrue(is_date("2022-10-0"))
        self.assertFalse(is_date("2022-100-10"))
        self.assertFalse(is_date("2022-10-100"))
        self.assertFalse(is_date("2022asd-10-10"))
        self.assertFalse(is_date("2022-10asd-10"))
        self.assertFalse(is_date("2022-10-10asd"))
        self.assertFalse(is_date("asd-das-das"))
        self.assertFalse(is_date("das-10-10"))
        self.assertFalse(is_date("2022-das-10"))
        self.assertFalse(is_date("2022-10-das"))