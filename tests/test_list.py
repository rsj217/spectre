#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'

import unittest
from structure.sequence.list import List, Node


class TestNode(unittest.TestCase):

    def test_node(self):
        n = Node()
        self.assertIsNone(n.data)
        self.assertIsNone(n.pred)
        self.assertIsNone(n.succ)


class TestList(unittest.TestCase):

    def test_empty(self):
        l = List()
        self.assertTrue(l.empty)
        self.assertEqual(l.size, 0)

    def test_header_trailer(self):
        l = List()
        self.assertEqual(l._header.succ, l._tailer)
        self.assertIsNone(l._header.pred)

        self.assertEqual(l._tailer.pred, l._header)
        self.assertIsNone(l._tailer.succ)

    def test_insert_as_first_pred_succ_first_last(self):
        l = List()
        n1 = l.insert_as_first(1)

        self.assertEqual(l.size, 1)
        self.assertEqual(n1.data, 1)
        self.assertEqual(l.first, n1)
        self.assertEqual(l.last, n1)

        self.assertEqual(l._header.succ, n1)
        self.assertEqual(l._header, n1.pred)

        self.assertEqual(n1.succ, l._tailer)
        self.assertEqual(n1, l._tailer.pred)

    def test_insert_as_last(self):
        l = List()
        n1 = l.insert_as_last(1)

        self.assertEqual(l.size, 1)
        self.assertEqual(n1.data, 1)
        self.assertEqual(l.last, n1)
        self.assertEqual(n1, l.last)

        self.assertEqual(n1.pred, l._header)
        self.assertEqual(n1, l._header.succ)

        self.assertEqual(n1.succ, l._tailer)
        self.assertEqual(n1, l._tailer.pred)

    def test_insert_before(self):
        l = List()
        n2 = l.insert_as_first(2)
        n1 = l.insert_before(n2, 1)
        self.assertEqual(l.size, 2)

        self.assertEqual(n1.succ, n2)
        self.assertEqual(n1, n2.pred)

        self.assertEqual(l.first, n1)
        self.assertEqual(l.last, n2)

        self.assertEqual(n1.pred, l._header)
        self.assertEqual(n2.succ, l._tailer)

    def test_insert_after(self):
        l = List()
        n2 = l.insert_as_first(2)
        n1 = l.insert_before(n2, 1)
        n3 = l.insert_after(n2, 3)

        self.assertEqual(l.size, 3)
        self.assertEqual(n2.succ, n3)
        self.assertEqual(n2, n3.pred)

        self.assertEqual(l.last, n3)
        self.assertEqual(l.last.succ, l._tailer)

    def test_visit(self):
        l = List()

        n2 = l.insert_as_first(2)
        n1 = l.insert_before(n2, 1)
        n3 = l.insert_after(n2, 3)

        r = [i.data for i in l]
        self.assertEqual(r, [1, 2, 3])

    def test_get(self):
        l = List()
        try:
            l[0]
        except AssertionError as e:
            self.assertEqual(AssertionError, type(e))
            self.assertEqual(e.args[0], 'index error')

        n2 = l.insert_as_first(2)
        n1 = l.insert_before(n2, 1)
        n3 = l.insert_after(n2, 3)

        self.assertEqual(l[0], n1)
        self.assertEqual(l[1], n2)
        self.assertEqual(l[2], n3)

    def test_remove(self):
        l = List()
        n2 = l.insert_as_first(2)
        n1 = l.insert_before(n2, 1)
        n3 = l.insert_after(n2, 3)

        self.assertEqual(l[1], n2)

        l.remove(n2)
        self.assertEqual(l.size, 2)
        self.assertEqual(n1.succ, n3)
        self.assertEqual(n1, n3.pred)

        self.assertEqual(l[1], n3)

        self.assertEqual(l[0], n1)
        l.remove(n1)
        self.assertEqual(l.size, 1)
        self.assertEqual(l.first, n3)
        self.assertEqual(l.last, n3)
        self.assertEqual(l[0], n3)

        self.assertEqual(l._header.succ, n3)
        self.assertEqual(l._header, n3.pred)

        l.remove(n3)
        self.assertEqual(l.size, 0)
        self.assertEqual(l.first, l._tailer)
        self.assertEqual(l.last, l._header)

        try:
            l[0]
        except AssertionError as e:
            self.assertEqual(AssertionError, type(e))
            self.assertEqual(e.args[0], 'index error')

    def test_find(self):
        l = List()
        n2 = l.insert_as_first(2)
        n1 = l.insert_before(n2, 1)
        n3 = l.insert_after(n2, 3)
        n4 = l.insert_after(n3, 3)

        r = l.find(1)
        self.assertEqual(n1, r)

        r = l.find(3)
        self.assertEqual(n3, r)

        r = l.find(-1)
        self.assertEqual(r, -1)

        r = l.find(5)
        self.assertEqual(r, -1)

    def test_reverse(self):
        l = List()
        n5 = l.insert_as_first(5)
        for i in range(5):
            l.insert_before(n5, i)

        l.reverse()
        r = [i.data for i in l]
        self.assertEqual(r, [5, 4, 3, 2, 1, 0])

        self.assertEqual(l.first.data, 5)
        self.assertEqual(l.last.data, 0)
        self.assertEqual(l._header.succ, l[0])
        self.assertIsNone(l._header.pred)
        self.assertEqual(l._tailer.pred, l[5])
        self.assertIsNone(l._tailer.succ)


if __name__ == '__main__':
    unittest.main()
