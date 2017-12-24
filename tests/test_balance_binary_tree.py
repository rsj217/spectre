#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from tree.balance_binary_search_tree import AVLTree


class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.avl = AVLTree()

    def test_gen_tree(self):
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

        print('hot', self.avl.hot)

        g = self.avl.trave_in()
        for i in g:
            self.assertTrue(self.avl.avl_balanced(i))


if __name__ == '__main__':
    unittest.main()
