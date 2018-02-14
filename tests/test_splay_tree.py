#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from spectre.tree.node import Entry
from spectre.tree.splay_tree import SplayTree
from spectre.tree.binary_search_tree import BinarySearchTree


class TestSplayTreeSearch(unittest.TestCase):

    def setUp(self):
        self.st = SplayTree()

    def test_search_zig(self):
        bst = BinarySearchTree()
        e20 = Entry(key=20, value=20)
        e21 = Entry(key=21, value=21)
        e17 = Entry(key=17, value=17)
        e12 = Entry(key=12, value=12)
        e16 = Entry(key=16, value=16)

        n20 = bst.insert_as_root(e20)
        n21 = bst.insert(e21)
        n17 = bst.insert(e17)
        n12 = bst.insert(e12)
        n16 = bst.insert(e16)

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
        e20 = Entry(key=20, value=20)
        e25 = Entry(key=25, value=25)
        e17 = Entry(key=17, value=17)
        e23 = Entry(key=23, value=23)
        e28 = Entry(key=28, value=28)

        n20 = bst.insert_as_root(e20)
        n25 = bst.insert(e25)
        n17 = bst.insert(e17)
        n23 = bst.insert(e23)
        n28 = bst.insert(e28)

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
        e20 = Entry(key=20, value=20)
        e21 = Entry(key=21, value=21)
        e17 = Entry(key=17, value=17)
        e12 = Entry(key=12, value=12)
        e14 = Entry(key=14, value=14)
        e10 = Entry(key=10, value=10)
        e18 = Entry(key=18, value=18)
        e13 = Entry(key=13, value=13)
        e15 = Entry(key=15, value=15)

        n20 = bst.insert_as_root(e20)
        n21 = bst.insert(e21)
        n17 = bst.insert(e17)
        n12 = bst.insert(e12)
        n14 = bst.insert(e14)
        n10 = bst.insert(e10)
        n18 = bst.insert(e18)
        n13 = bst.insert(e13)
        n15 = bst.insert(e15)

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
        e20 = Entry(key=20, value=20)
        e25 = Entry(key=25, value=25)
        e15 = Entry(key=15, value=15)
        e23 = Entry(key=23, value=23)
        e30 = Entry(key=30, value=30)
        e27 = Entry(key=27, value=27)
        e35 = Entry(key=35, value=35)
        e26 = Entry(key=26, value=26)
        e29 = Entry(key=29, value=29)


        n20 = bst.insert_as_root(e20)
        n25 = bst.insert(e25)
        n15 = bst.insert(e15)
        n23 = bst.insert(e23)
        n30 = bst.insert(e30)
        n27 = bst.insert(e27)
        n35 = bst.insert(e35)
        n26 = bst.insert(e26)
        n29 = bst.insert(e29)

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
        e20 = Entry(key=20, value=20)
        e25 = Entry(key=25, value=25)
        e15 = Entry(key=15, value=15)
        e23 = Entry(key=23, value=23)
        e30 = Entry(key=30, value=30)
        e27 = Entry(key=27, value=27)
        e35 = Entry(key=35, value=35)
        e26 = Entry(key=26, value=26)
        e29 = Entry(key=29, value=29)


        n20 = bst.insert_as_root(e20)
        n25 = bst.insert(e25)
        n15 = bst.insert(e15)
        n23 = bst.insert(e23)
        n30 = bst.insert(e30)
        n27 = bst.insert(e27)
        n35 = bst.insert(e35)
        n26 = bst.insert(e26)
        n29 = bst.insert(e29)

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
        e20 = Entry(key=20, value=20)
        e21 = Entry(key=21, value=21)
        e17 = Entry(key=17, value=17)
        e12 = Entry(key=12, value=12)
        e14 = Entry(key=14, value=14)
        e10 = Entry(key=10, value=10)
        e18 = Entry(key=18, value=18)
        e13 = Entry(key=13, value=13)
        e15 = Entry(key=15, value=15)

        n20 = bst.insert_as_root(e20)
        n21 = bst.insert(e21)
        n17 = bst.insert(e17)
        n12 = bst.insert(e12)
        n14 = bst.insert(e14)
        n10 = bst.insert(e10)
        n18 = bst.insert(e18)
        n13 = bst.insert(e13)
        n15 = bst.insert(e15)

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
