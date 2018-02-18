#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from spectre.tree.node import BTNode
from spectre.tree.multi_search_tree import BTree


def gen_a_btree():
    """
                 53
        36              7789

    19    4151      75  7984  97
    """
    n53 = BTNode()
    n53.insert_as_root(key=53)

    n36 = BTNode(parent=n53)
    n36._key = [36]

    n7789 = BTNode(parent=n53)
    n7789._key = [77, 89]
    n53._child = [n36, n7789]

    n19 = BTNode(parent=n36)
    n19._key = [19]
    n19._child.append(None)

    n4151 = BTNode(parent=n36)
    n4151._key = [41, 51]
    n4151._child = [None, None, None]

    n36._child = [n19, n4151]

    n75 = BTNode(parent=n7789)
    n75._key = [75]
    n75._child = [None, None]

    n97 = BTNode(parent=n7789)
    n97._key = [97]
    n97._child = [None, None]

    n7984 = BTNode(parent=n7789)
    n7984._key = [79, 84]
    n7984._child = [None, None, None]

    n7789._child = [n75, n7984, n97]

    bt = BTree()
    bt.insert_as_root(n53)
    bt._size = 8

    return bt


class TestBTree(unittest.TestCase):

    def setUp(self):
        pass

    def test_search(self):
        bt = gen_a_btree()
        n53 = bt.search(53)
        self.assertEqual(n53, bt.root)
        self.assertIsNone(n53.parent)
        self.assertEqual(n53.key, [53])

        n36 = bt.search(36)
        n77 = bt.search(77)
        n89 = bt.search(89)

        self.assertEqual(n77, n89)
        self.assertEqual(n77.parent, n53)
        self.assertEqual(n36.parent, n53)
        self.assertEqual(n53.child, [n36, n77])

        n19 = bt.search(19)
        self.assertEqual(n19.parent, n36)
        self.assertEqual(n19.child, [None, None])

        n41 = bt.search(41)
        self.assertEqual(n41.key, [41, 51])
        self.assertEqual(n41.parent, n36)
        self.assertEqual(n41.child, [None, None, None])

    def test_inorder(self):
        bt = gen_a_btree()
        self.assertEqual([i for i in bt], [19, 36, 41, 51, 53, 75, 77, 79, 84, 89, 97])

    def test_insert_without_overflow(self):
        bt = gen_a_btree()
        r = bt.search(23)
        self.assertIsNone(r)

        r = bt.insert(23)
        self.assertTrue(r)
        self.assertEqual(bt.size, 9)

        self.assertEqual([i for i in bt], [19, 23, 36, 41, 51, 53, 75, 77, 79, 84, 89, 97])

        n23 = bt.search(23)
        print(n23)

    def test_insert_overflow(self):
        bt = gen_a_btree()
        r = bt.search(23)
        self.assertIsNone(r)

        r = bt.insert(23)
        self.assertTrue(r)
        self.assertEqual(bt.size, 9)

        self.assertEqual([i for i in bt], [19, 23, 36, 41, 51, 53, 75, 77, 79, 84, 89, 97])

        r = bt.insert(29)
        self.assertTrue(r)
        self.assertEqual(bt.size, 10)
        self.assertEqual([i for i in bt], [19, 23, 29, 36, 41, 51, 53, 75, 77, 79, 84, 89, 97])

        n29 = bt.search(29)
        print(n29)
        self.assertEqual(n29.parent.key, [23, 36])

        n19 = bt.search(19)
        print(n19)

        n23 = bt.search(23)
        n36 = bt.search(36)
        self.assertEqual(n23, n36)

        n4151 = bt.search(41)

        self.assertEqual(n23.child, [n19, n29, n4151])

        bt.insert(45)
        n45 = bt.search(45)
        print(n45)
        self.assertEqual([i for i in bt], [19, 23, 29, 36, 41, 45, 51, 53, 75, 77, 79, 84, 89, 97])

        bt.insert(87)
        print(bt.root)
        self.assertEqual([i for i in bt], [19, 23, 29, 36, 41, 45, 51, 53, 75, 77, 79, 84, 87, 89, 97])
        n53 = bt.search(53)
        self.assertEqual(bt.root, n53)


if __name__ == '__main__':
    unittest.main()
