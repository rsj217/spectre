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

    bt = BTree()
    for key in [53, 36, 77, 89, 19, 41, 51, 75, 97, 79, 84]:
        bt.insert(key)
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
        self.assertEqual(bt.size, 12)

        self.assertEqual([i for i in bt], [19, 23, 36, 41, 51, 53, 75, 77, 79, 84, 89, 97])

        n23 = bt.search(23)
        print(n23)

    def test_insert_overflow(self):
        bt = gen_a_btree()
        r = bt.search(23)
        self.assertIsNone(r)

        r = bt.insert(23)
        self.assertTrue(r)
        self.assertEqual(bt.size, 12)

        self.assertEqual([i for i in bt], [19, 23, 36, 41, 51, 53, 75, 77, 79, 84, 89, 97])

        r = bt.insert(29)
        self.assertTrue(r)
        self.assertEqual(bt.size, 13)
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
