#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from tree.balance_binary_search_tree import AVLTree


class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.avl = AVLTree()

    def test_insert_node(self):
        """
        <AVLTree>(
              58
          53      69
        40  54
        )
        """
        root = self.avl.insert_as_root(58)

        self.avl.insert(53)
        self.avl.insert(40)
        self.avl.insert(69)
        self.avl.insert(54)
        self.avl.insert(30)
        self.avl.insert(20)

        g = self.avl.trave_level()
        for i in g:
            self.assertTrue(self.avl.avl_balanced(i))

    def test_remove_node(self):
        """
        <AVLTree>(
                      53
              30              58
          20      40      54      69
        )
        """
        root = self.avl.insert_as_root(50)

        self.avl.insert(30)
        self.avl.insert(58)
        self.avl.insert(20)
        self.avl.insert(54)
        self.avl.insert(69)
        self.avl.insert(52)

        self.avl.remove(69)
        g = self.avl.trave_level()
        for i in g:
            self.assertTrue(self.avl.avl_balanced(i))


if __name__ == '__main__':
    unittest.main()
