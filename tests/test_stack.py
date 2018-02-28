#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'

import unittest
from spectre.sequence.stack import Stack


class TestStack(unittest.TestCase):

    def test_empty(self):
        s = Stack(size=0, capacity=4)
        self.assertTrue(s.empty)
        self.assertEqual(s.size, 0)

    def test_push_top_pop(self):
        s = Stack(size=0, capacity=3)
        s.push(0)
        s.push(1)
        s.push(2)
        self.assertEqual(s.size, 3)

        t = s.top
        self.assertEqual(t, 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(s.pop(), 0)

        for i in range(3):
            s.push(i)

        s.push(3)
        self.assertEqual(s.top, 3)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.cap, 6)


if __name__ == '__main__':
    unittest.main()
