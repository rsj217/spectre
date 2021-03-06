#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'

import unittest
from spectre.sequence.vector import Vector


class TestVector(unittest.TestCase):

    def test_empty_vector(self):
        v = Vector(size=0, capacity=0)
        self.assertTrue(v.empty)
        self.assertEqual(v.size, 0)
        self.assertEqual(v._capacity, 0)

    def test_size(self):
        v = Vector(size=2, capacity=4)
        self.assertFalse(v.empty)
        self.assertEqual(v.size, 2)
        self.assertEqual(v.cap, 4)

    def test_get_put(self):
        v = Vector(size=2, capacity=4)
        self.assertEqual(v[0], 0)
        v[1] = 11
        self.assertEqual(v[1], 11)

    def test_put_error(self):
        v = Vector(size=2, capacity=4)
        v[0] = 0
        v[1] = 1
        try:
            v[2] = 2
        except AssertionError as e:
            self.assertEqual(AssertionError, type(e))

        try:
            v[10]
        except Exception as e:
            self.assertNotEqual(AssertionError, type(e))
            self.assertEqual(IndexError, type(e))

    def test_expand(self):
        v = Vector(size=2, capacity=2)
        self.assertEqual(v.data, [0, 0])
        v.expand()
        self.assertEqual(v.size, 2)
        self.assertEqual(v.cap, 4)

    def test_insert(self):
        v = Vector(size=0, capacity=3)
        v.insert(0, 9)
        self.assertEqual(v.size, 1)
        self.assertEqual(v.data, [9])
        v.insert(0, 4)
        self.assertEqual(v.data, [4, 9])
        v.insert(1, 5)
        self.assertEqual(v.data, [4, 5, 9])
        v[1] = 2
        self.assertEqual(v.data, [4, 2, 9])
        self.assertEqual(v[1], 2)
        v.insert(3, 6)
        self.assertEqual(v.size, 4)
        self.assertEqual(v.cap, 6)
        self.assertEqual(v.data, [4, 2, 9, 6])
        v.insert(1, 7)

    def test_remove(self):
        v = Vector(size=0, capacity=3)
        v.insert(0, 9)
        self.assertEqual(v.size, 1)
        v.insert(0, 4)
        v.insert(1, 5)
        self.assertEqual(v.data, [4, 5, 9])
        v[1] = 2
        self.assertEqual(v.data, [4, 2, 9])
        self.assertEqual(v[1], 2)
        v.insert(3, 6)
        self.assertEqual(v.size, 4)
        self.assertEqual(v.cap, 6)
        v.insert(1, 7)
        self.assertEqual(v.remove(2), 2)
        self.assertEqual(v.data, [4, 7, 9, 6])

        v.insert(1, 3)
        self.assertEqual(v.data, [4, 3, 7, 9, 6])

        v.insert(3, 4)
        self.assertEqual(v.data, [4, 3, 7, 4, 9, 6])
        self.assertEqual(v.data, [4, 3, 7, 4, 9, 6])

    def test_find(self):
        v = Vector(capacity=6)
        for i in [6, 9, 4, 7, 3, 4]:
            v.insert(0, i)
        print(v)
        self.assertEqual(v.find(4), 0)
        self.assertEqual(v.find(9), 4)
        self.assertEqual(v.find(5), -1)

    def test_find_range(self):
        v = Vector(capacity=6)
        for i in [6, 9, 4, 7, 3, 4]:
            v.insert(0, i)
        print(v)
        self.assertEqual(v.find(4, 0, 5), 0)
        self.assertEqual(v.find(9, 0, 5), 4)
        self.assertEqual(v.find(9, 0, 4), -1)
        self.assertEqual(v.find(5), -1)

    def test_deduplicate(self):
        v = Vector(capacity=6)
        for i in [6, 9, 4, 7, 3, 6, 6, 7, 1, 4]:
            v.insert(0, i)
        # print(v)
        old_size = v.size
        size = v.deduplicate()
        # print(v)
        new_size = v.size
        self.assertEqual(old_size - new_size, size)
        size = v.deduplicate()
        self.assertEqual(size, 0)

    def test_low_uniquify(self):
        v = Vector(capacity=10)
        for i in [6, 6, 6, 5, 5, 3, 3, 3, 1, 1]:
            v.insert(0, i)
        print(v)
        s = v.low_uniquify()
        self.assertEqual(s, 6)
        self.assertEqual(v.data, [1, 3, 5, 6])

    def test_uniquify(self):
        v = Vector(capacity=10)
        for i in [13, 13, 13, 13, 8, 8, 8, 5, 5, 5, 5, 5, 3, 3, 3, 3]:
            v.insert(0, i)
        print(v)
        s = v.uniquify()
        self.assertEqual(s, 12)
        self.assertEqual(v.data, [3, 5, 8, 13])

    def test_travel(self):
        v = Vector(capacity=6)
        for i in [6, 9, 4, 7, 3, 6, 6, 7, 1, 4]:
            v.insert(0, i)
        s = []
        for i in v:
            s.append(i)

        self.assertEqual(s, [4, 1, 7, 6, 6, 3, 7, 4, 9, 6])

    def test_disordered(self):
        v = Vector(capacity=6)
        for i in [6, 9, 4, 7, 3, 1]:
            v.insert(0, i)
        # print(v)
        print(v.disordered())
        self.assertEqual(v.disordered(), 2)

        v = Vector(capacity=6)
        for i in range(5, 0, -1):
            v.insert(0, i)
        # print(v)
        self.assertEqual(v.disordered(), 0)

        v = Vector(capacity=6)
        for i in [6, 9, 4, 7, 3, 6, 6, 7, 1, 4]:
            v.insert(0, i)
        # print(v)
        self.assertEqual(v.disordered(), 5)


if __name__ == '__main__':
    unittest.main()
