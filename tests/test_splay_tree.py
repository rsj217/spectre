#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from tree.splay_tree import SplayTree
from tree.binary_search_tree import BinarySearchTree


class TestSplayTreeSearch(unittest.TestCase):

    def setUp(self):
        self.st = SplayTree()

    def test_search_zig(self):
        bst = BinarySearchTree()
        n20 = bst.insert_as_root(20)
        n21 = bst.insert(21)
        n17 = bst.insert(17)
        n12 = bst.insert(12)
        n16 = bst.insert(16)

        self.st._root = n20
        self.st._size = bst.size
        del bst
        print(self.st)
        self.st.search(n17.key)
        print(self.st)
        for i in self.st.inorder(self.st.root):
            print(i)

    def test_search_zag(self):
        bst = BinarySearchTree()
        n20 = bst.insert_as_root(20)
        n25 = bst.insert(25)
        n17 = bst.insert(17)
        n23 = bst.insert(23)
        n28 = bst.insert(28)

        self.st._root = n20
        self.st._size = bst.size
        del bst
        print(self.st)

        self.st.search(n25.key)
        print(self.st)
        for i in self.st.inorder(self.st.root):
            print(i)

        self.assertEqual(self.st.root, n25)

    def test_search_zig_zig(self):
        bst = BinarySearchTree()
        n20 = bst.insert_as_root(20)
        n21 = bst.insert(21)
        n17 = bst.insert(17)
        n12 = bst.insert(12)
        n14 = bst.insert(14)
        n10 = bst.insert(10)
        n18 = bst.insert(18)
        n13 = bst.insert(13)
        n15 = bst.insert(15)

        self.st._root = n20
        self.st._size = bst.size
        del bst
        print(self.st)
        self.st.search(n12.key)
        print(self.st)
        for i in self.st.inorder(self.st.root):
            print(i)

        print(self.st.root)
        self.assertEqual(self.st.root, n12)

    def test_search_zag_zag(self):
        bst = BinarySearchTree()
        n20 = bst.insert_as_root(20)
        n25 = bst.insert(25)
        n15 = bst.insert(15)
        n23 = bst.insert(23)
        n30 = bst.insert(30)
        n27 = bst.insert(27)
        n35 = bst.insert(35)
        n26 = bst.insert(26)
        n29 = bst.insert(29)

        self.st._root = n20
        self.st._size = bst.size
        del bst
        print(self.st)

        self.st.search(n30.key)
        print(self.st)
        for i in self.st.inorder(self.st.root):
            print(i)

        self.assertEqual(self.st.root, n30)

    def test_search_zig_zag_and_zag(self):
        bst = BinarySearchTree()
        n20 = bst.insert_as_root(20)
        n25 = bst.insert(25)
        n15 = bst.insert(15)
        n23 = bst.insert(23)
        n30 = bst.insert(30)
        n27 = bst.insert(27)
        n35 = bst.insert(35)
        n26 = bst.insert(26)
        n29 = bst.insert(29)

        self.st._root = n20
        self.st._size = bst.size
        del bst
        print(self.st)

        self.st.search(n27.key)
        print(self.st)
        for i in self.st.inorder(self.st.root):
            print(i)

    def test_search_zag_zig_and_zig(self):
        bst = BinarySearchTree()
        n20 = bst.insert_as_root(20)
        n21 = bst.insert(21)
        n17 = bst.insert(17)
        n12 = bst.insert(12)
        n14 = bst.insert(14)
        n10 = bst.insert(10)
        n18 = bst.insert(18)
        n13 = bst.insert(13)
        n15 = bst.insert(15)

        self.st._root = n20
        self.st._size = bst.size
        del bst
        print(self.st)
        self.st.search(n14.key)
        print(self.st)
        for i in self.st.inorder(self.st.root):
            print(i)

        self.assertEqual(self.st.root, n14)


if __name__ == '__main__':
    unittest.main()
