#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'

import unittest
from spectre.sequence.queue import Queue


class TestQueue(unittest.TestCase):

    def test_empty(self):
        q = Queue()
        self.assertTrue(q.empty)
        self.assertEqual(q.size, 0)

    def test_enqueue_front_dequeue(self):
        q = Queue()

        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)

        self.assertEqual(q.size, 3)

        f = q.front
        self.assertEqual(f, 0)
        self.assertEqual(q.dequeue(), 0)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.size, 0)

        try:
            q.dequeue()
        except AssertionError as e:
            self.assertEqual(AssertionError, type(e))


if __name__ == '__main__':
    unittest.main()
