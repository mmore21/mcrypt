import unittest
from mcrypt.math import gcd

class TestMath(unittest.TestCase):
    def setUp(self):
        pass

    def test_gcd(self):
        self.assertEqual(gcd(24, 36), 12)

