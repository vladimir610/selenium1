# -*- coding=utf-8 -*-

from unittest import TestCase
import unittest

class TestAbc(TestCase):
    ''' Class testov abs'''
    def test_abs1():
        assert abs(-42) == 42, "Should be absolute value of a number" 

    def test_abs2():
        assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    unittest.main()
    