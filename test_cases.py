#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample1 (self):
                self.assertEqual (1, calc(1,1))
        def test_sample2 (self):
                self.assertEqual (998001, calc(999,999))
        def test_sample3 (self):
                self.assertEqual (-1, calc(0,500))
        def test_sample4 (self):
                self.assertEqual (-1, calc(1000,500))
        def test_sample5 (self):
                self.assertEqual (-1, calc(0.1,500))
        def test_sample6 (self):
                self.assertEqual (-1, calc("a", 500))
        def test_sample7 (self):
                self.assertEqual (-1, calc(None, 500))                            
        def test_sample8 (self):
                self.assertEqual (-1, calc(999999999, 500))
        def test_sample9 (self):
                self.assertEqual (-1, calc(-999999999, 500))
