#!/usr/bin/python3
""" Unit test for base"""


import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test square"""
    def test_square(self):
        s1 = Square(5)
        self.assertEqual(s1.id, 1)
