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

        node = self.avl.insert_e(30)
        # node = self.avl.insert_e(20)

        # self.avl._root = node.parent.parent

        g = self.avl.trave_level()
        for i in g:
            self.assertTrue(self.avl.avl_balanced(i))
            print(i.key, i.height)

        print(self.avl.root)
        print(self.avl)





if __name__ == '__main__':
    unittest.main()
