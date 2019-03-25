from unittest import TestCase
from Bruteforce.password import Password

class TestPassword(TestCase):
    def test_check1(self):
        pwd=Password("abc")
        self.assertEqual(True,pwd.check("abc"))

    def test_check2(self):
        pwd=Password("abc")
        self.assertEqual(False,pwd.check("bddb"))