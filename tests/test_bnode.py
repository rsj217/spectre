#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from tree.node import BinNode
from tree.binary_tree import BinaryTree


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = BinNode()

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


if __name__ == '__main__':
    unittest.main()
