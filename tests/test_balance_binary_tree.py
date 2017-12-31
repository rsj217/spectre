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
              53
          40      58
                54  69
        )
        """
        root = self.avl.insert_as_root(58)

        self.avl.insert(53)
        self.avl.insert(40)
        self.avl.insert(69)
        self.avl.insert(54)
        print(self.avl)
        g = self.avl.trav_levelorder(self.avl.root)
        for i in g:
            self.assertTrue(self.avl.avl_balanced(i))

    def test_remove_node(self):
        """
        <AVLTree>(
                      50
              30              58
          20              54      69
                        52
        )

        <AVLTree>(
              50
          30      54
        20      52  58
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
        print(self.avl)
        g = self.avl.trav_levelorder(self.avl.root)
        for i in g:
            self.assertTrue(self.avl.avl_balanced(i))


if __name__ == '__main__':
    unittest.main()
