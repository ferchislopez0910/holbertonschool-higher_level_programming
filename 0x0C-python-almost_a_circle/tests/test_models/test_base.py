#!/usr/bin/python3
""" Unit test for base"""


import unittest
from models.base import Base


class TestBaseModels(unittest.TestCase):
    """ class def test"""
    def test_base(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b4 = Base(6)
        self.assertEqual(b4.id, 6)
