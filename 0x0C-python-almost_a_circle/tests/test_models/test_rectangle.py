#!/usr/bin/python3
""" Unit test for base"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def Rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def Raises(self):
        r1 = Rectangle("10", 2)
        self.assertRaises(TypeError, r1.width)
        r2 = Rectangle(10, -2)
        self.assertRaises(ValueError, r2.height)
        r3 = Rectangle(10, 2, 3, -1)
        self.assertRaises(ValueError, r3.x)

    def area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)
