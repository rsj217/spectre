#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'

import unittest
from sequence.vector import Vector


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
        self.assertEqual(v._elem, [0, 0, None, None])

    def test_get_put(self):
        v = Vector(size=2, capacity=4, value=10)
        self.assertEqual(v[0], 10)
        v[1] = 11
        self.assertEqual(v[1], 11)
        self.assertIsNone(v[2])

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
            self.assertNotEquals(AssertionError, type(e))
            self.assertEqual(IndexError, type(e))

    def test_expand(self):
        v = Vector(size=2, capacity=2, value=10)
        self.assertEqual(v._elem, [10, 10])
        v.expand()
        self.assertEqual(v.size, 2)
        self.assertEqual(v.cap, 4)
        self.assertEqual(v._elem, [10, 10, None, None])

    def test_insert(self):
        v = Vector(size=0, capacity=3)
        v.insert(0, 9)
        self.assertEqual(v.size, 1)
        self.assertEqual(v._elem,  [9, None, None])
        self.assertEqual((v.data, [9]))
        v.insert(0, 4)
        self.assertEqual(v._elem,  [4, 9, None])
        self.assertEqual(v.data,  [4, 9])
        v.insert(1, 5)
        self.assertEqual(v._elem,  [4, 5, 9])
        v[1] = 2
        self.assertEqual(v._elem,  [4, 2, 9])
        self.assertEqual(v[1], 2)
        v.insert(3, 6)
        self.assertEqual(v.size, 4)
        self.assertEqual(v.cap, 6)
        self.assertEqual(v._elem, [4, 2, 9, 6, None, None])
        self.assertEqual(v.data, [4, 2, 9, 6])
        v.insert(1, 7)
        self.assertEqual(v._elem, [4, 7, 2, 9, 6, None])

    def test_remove(self):
        v = Vector(size=0, capacity=3)
        v.insert(0, 9)
        self.assertEqual(v.size, 1)
        self.assertEqual(v._elem,  [9, None, None])
        v.insert(0, 4)
        self.assertEqual(v._elem,  [4, 9, None])
        v.insert(1, 5)
        self.assertEqual(v._elem,  [4, 5, 9])
        v[1] = 2
        self.assertEqual(v._elem,  [4, 2, 9])
        self.assertEqual(v[1], 2)
        v.insert(3, 6)
        self.assertEqual(v.size, 4)
        self.assertEqual(v.cap, 6)
        self.assertEqual(v._elem, [4, 2, 9, 6, None, None])
        v.insert(1, 7)
        self.assertEqual(v._elem, [4, 7, 2, 9, 6, None])
        self.assertEqual(v.remove(2), 2)
        self.assertEqual(v._elem, [4, 7, 9, 6, None, None])
        self.assertEqual(v.data, [4, 7, 9, 6])

        v.insert(1, 3)
        self.assertEqual(v._elem, [4, 3, 7, 9, 6, None])
        self.assertEqual(v.data, [4, 3, 7, 9, 6])

        v.insert(3, 4)
        self.assertEqual(v._elem, [4, 3, 7, 4, 9, 6])
        self.assertEqual(v.data, [4, 3, 7, 4, 9, 6])

if __name__ == '__main__':
    unittest.main()
