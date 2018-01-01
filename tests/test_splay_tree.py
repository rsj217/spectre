#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from tree.splay_tree import SplayTree
from tree.binary_search_tree import BinarySearchTree


class TestSplayTree(unittest.TestCase):

    def setUp(self):
        self.st = SplayTree()

    def test_search_zig(self):
        self.st.insert_as_root(15)
        n13 = self.st.insert(13)
        n14 = self.st.insert(14)
        n12 = self.st.insert(12)


        print(self.st)
        self.st.searche(n13.key)
        #
        print(self.st)

        for i in self.st.inorder(self.st.root):
            print(i)

    def test_search_zag(self):
        self.st.insert_as_root(15)
        n17 = self.st.insert(17)
        self.st.insert(16)
        self.st.insert(18)


        print(self.st)
        self.st.searche(n17.key)
        #
        print(self.st)

        # for i in self.st.inorder(self.st.root):
        #     print(i)

    def test_search_zig_zig(self):
        self.st.insert_as_root(15)
        self.st.insert(14)
        n13 = self.st.insert(13)


        print(self.st)
        self.st.searche(n13.key)

        print(self.st)

        for i in self.st.inorder(self.st.root):
            print(i)


    def test_search_zag_zag(self):
        self.st.insert_as_root(15)
        n17 = self.st.insert(17)
        self.st.insert(16)
        n19 = self.st.insert(19)
        n18 = self.st.insert(18)
        n20 = self.st.insert(20)

        print(self.st)
        self.st.searche(n19.key)

        print(self.st)

        for i in self.st.inorder(self.st.root):
            print(i)


    def test_search_zag_zig(self):
        self.st.insert_as_root(15)
        n11 = self.st.insert(11)
        n10 = self.st.insert(10)
        n13 = self.st.insert(13)
        n12 = self.st.insert(12)
        n14 = self.st.insert(14)

        print(self.st)
        self.st.searche(n13.key)

        print(self.st)

        for i in self.st.inorder(self.st.root):
            print(i)

    def test_search_zig_zag(self):
        bst = BinarySearchTree()
        r = bst.insert_as_root(15)
        n20 = bst.insert(20)
        n18 = bst.insert(18)
        n13 = bst.insert(10)
        n12 = bst.insert(21)
        n14 = bst.insert(16)
        n14 = bst.insert(19)

        self.st._root = r
        self._size = bst.size


        print(self.st)
        self.st.searche(n18.key)
        #
        print(self.st)
        #
        # for i in self.st.inorder(self.st.root):
        #     print(i)


    def test_search_zig_zag_gg_rchild(self):
        bst = BinarySearchTree()
        r = bst.insert_as_root(14)
        n15 = bst.insert(15)
        n20 = bst.insert(20)
        n18 = bst.insert(18)
        n21 = bst.insert(21)
        n16 = bst.insert(16)
        n19 = bst.insert(19)
        n12 = bst.insert(12)
        n12 = bst.insert(11)

        self.st._root = r
        self._size = bst.size


        print(self.st)
        self.st.searche(n18.key)
        #
        print(self.st)
        #
        # for i in self.st.inorder(self.st.root):
        #     print(i)


if __name__ == '__main__':
    unittest.main()
