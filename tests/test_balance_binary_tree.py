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

    def test_zig(self):
        root = self.avl.insert_as_root(57)
        n36 = self.avl.inserte(36)
        n23 = self.avl.inserte(23)
        n11 = self.avl.inserte(11)
        n18 = self.avl.inserte(18)
        print(self.avl)
        #
        # n11.zag()
        # self.avl.update_height_above(n11)
        # print(self.avl)
        # n23.zig()
        # # self.avl.update_height_above(n23)
        # print(self.avl)

        g = self.avl.inorder(self.avl._root)
        for i in g:
            print(i)
        # print(root, n36, n36.lchild)


if __name__ == '__main__':
    unittest.main()
