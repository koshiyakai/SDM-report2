#!/usr/bin/python3

import unittest
from calc_mul import calc
# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample01 (self):
                self.assertEqual (500, calc(1,500))
        def test_sample02 (self):
                self.assertEqual (499500, calc(999,500))
        def test_sample03 (self):
                self.assertEqual (-1, calc(0,500))
        def test_sample04 (self):
                self.assertEqual (-1, calc(1000,500))
        def test_sample05 (self):
                self.assertEqual (-1, calc(0.1,500))
        def test_sample06 (self):
                self.assertEqual (-1, calc("a", 500))
        def test_sample07 (self):
                self.assertEqual (-1, calc(None, 500))                            
        def test_sample08 (self):
                self.assertEqual (12, calc(3, 4))
        def test_sample09 (self):
                self.assertEqual (12, calc(4, 3))                
