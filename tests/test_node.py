#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from spectre.tree.node import BinNode, BSNode, Entry


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = BinNode()

    def test_print_node(self):
        node = BinNode(data='node')
        self.assertEqual(node.__repr__(), '<BinNode>([None] None-node-None: 0)')

    def test_init_node(self):
        self.assertIsNone(self.node.parent)
        self.assertIsNone(self.node.lchild)
        self.assertIsNone(self.node.rchild)
        self.assertEqual(self.node.height, 0)
        self.assertEqual(self.node.deep, 0)
        self.assertEqual(self.node.size, 1, msg="node size error")

    def test_insert_as_left(self):
        node = self.node.insert_as_lc('left')
        self.assertEqual(node.data, 'left')
        self.assertEqual(self.node.lchild, node)
        self.assertEqual(node.parent, self.node)
        self.assertEqual(node.height, 0)
        self.assertEqual(node.size, 1)
        self.assertEqual(self.node.size, 2)
        self.assertEqual(node.deep, 1)
        self.assertEqual(self.node.deep, 0)

    def test_insert_as_right(self):
        node = self.node.insert_as_rc('right')
        self.assertEqual(node.data, 'right')
        self.assertEqual(self.node.rchild, node)
        self.assertEqual(node.height, 0)
        self.assertEqual(node.size, 1)
        self.assertEqual(self.node.size, 2)
        self.assertEqual(node.deep, 1)
        self.assertEqual(self.node.deep, 0)


class TestEntry(unittest.TestCase):

    def test_bsnode_lt(self):
        e1 = Entry(key=1, value=22)
        e2 = Entry(key=2, value=11)
        self.assertLess(e1, e2)

    def test_bsnode_lte(self):
        e1 = Entry(key=1, value=22)
        e2 = Entry(key=1, value=11)
        self.assertLessEqual(e1, e2)

    def test_bsnode_gt(self):
        e1 = Entry(key=2, value=22)
        e2 = Entry(key=1, value=11)
        self.assertGreater(e1, e2)

    def test_bsnode_gte(self):
        e1 = Entry(key=1, value=22)
        e2 = Entry(key=1, value=11)
        self.assertGreaterEqual(e1, e2)


class TestBSNode(unittest.TestCase):

    def test_print_node(self):
        entry = Entry(key=1, value=11)
        bsnode = BSNode(key=entry.key, value=entry.value)
        print(bsnode)
        self.assertEqual(bsnode.__repr__(), '<BSNode>([None] None-1-None: 0 - 11)')

    def test_bsnode_lt(self):
        b1 = BSNode(key=1, value=22)
        b2 = BSNode(key=2, value=11)
        self.assertLess(b1.key, b2.key)

    def test_bsnode_lte(self):
        b1 = BSNode(key=1, value=22)
        b2 = BSNode(key=1, value=11)
        self.assertLessEqual(b1.key, b2.key)

    def test_bsnode_gt(self):
        b1 = BSNode(key=2, value=22)
        b2 = BSNode(key=1, value=11)
        self.assertGreater(b1.key, b2.key)

    def test_bsnode_gte(self):
        b1 = BSNode(key=1, value=22)
        b2 = BSNode(key=1, value=11)
        self.assertGreaterEqual(b1.key, b2.key)


if __name__ == '__main__':
    unittest.main()
