#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from spectre.tree.node import Entry
from spectre.tree.binary_search_tree import BinarySearchTree


def gen_binary_search_tree():
    bst = BinarySearchTree()
    root = Entry(key=36, value='root')
    e27 = Entry(key=27, value=27)
    e16 = Entry(key=16, value=16)
    e58 = Entry(key=58, value=58)
    e53 = Entry(key=53, value=53)
    e40 = Entry(key=40, value=40)
    e46 = Entry(key=46, value=46)
    e69 = Entry(key=69, value=69)
    e64 = Entry(key=64, value=64)

    bst.insert_as_root(root)
    bst.insert(e27)
    bst.insert(e16)
    bst.insert(e58)
    bst.insert(e53)
    bst.insert(e40)
    bst.insert(e46)
    bst.insert(e69)
    bst.insert(e64)

    return bst


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

    def test_empty_tree(self):
        self.assertEqual(self.bst.root, None, msg='空树没有一个节点')
        self.assertEqual(self.bst.stature(self.bst.root), -1, msg="空树的高度为-1")
        self.assertEqual(self.bst.size, 0, msg='空树的size是0')
        self.assertEqual(self.bst.is_empty, True, msg='空树的empty返回True')

    def test_insert_root(self):
        e = Entry(key=10, value='root')
        root = self.bst.insert_as_root(e=e)
        self.assertEqual(self.bst.root, root)
        self.assertEqual(self.bst.root.value, 'root')
        self.assertEqual(root.height, 0)
        self.assertEqual(root.size, 1)
        self.assertEqual(self.bst.is_empty, False)
        self.assertEqual(self.bst.__repr__(), '''<BinarySearchTree>(
10
)''')

    def test_insert(self):
        bst = gen_binary_search_tree()
        print(bst)
        self.assertEqual(bst.size, 9)
        self.assertEqual(bst.root.height, 4)
        self.assertEqual(bst.root.lchild.height, 1)
        self.assertEqual(bst.__repr__(), """<BinarySearchTree>(
                              36
              27                              58
      16                              53              69
                                  40              64
                                    46
)""")

    def test_search(self):
        bst = gen_binary_search_tree()
        n53 = bst.search(53)
        self.assertEqual(n53.key, 53)
        self.assertEqual(n53.height, 2)

    def test_remove_without_child(self):
        bst = gen_binary_search_tree()
        bst.remove(16)
        self.assertEqual(bst.__repr__(), """<BinarySearchTree>(
                              36
              27                              58
                                      53              69
                                  40              64
                                    46
)""")

    def test_remove_with_lchild(self):
        bst = gen_binary_search_tree()
        bst.remove(27)
        self.assertEqual(bst.__repr__(), """<BinarySearchTree>(
                              36
              16                              58
                                      53              69
                                  40              64
                                    46
)""")

    def test_remove_with_rchild(self):
        bst = gen_binary_search_tree()
        bst.remove(40)
        self.assertEqual(bst.__repr__(), """<BinarySearchTree>(
              36
      27              58
  16              53      69
                46      64
)""")

    def test_remove_all_child(self):
        bst = gen_binary_search_tree()
        bst.remove(58)
        self.assertEqual(bst.__repr__(), """<BinarySearchTree>(
                              36
              27                              64
      16                              53              69
                                  40
                                    46
)""")
        n64 = bst.search(64)
        self.assertEqual(n64.value, 64)

    def test_remove_root(self):
        bst = gen_binary_search_tree()

        bst.remove(36)
        self.assertEqual(bst.__repr__(), """<BinarySearchTree>(
              40
      27              58
  16              53      69
                46      64
)""")
        self.assertEqual(bst.root.key, 40)
        self.assertEqual(bst.root.value, 40)

    def test_remove_as_rchild(self):
        bst = gen_binary_search_tree()
        print(bst)
        bst.remove(69)
        self.assertEqual(bst.__repr__(), """<BinarySearchTree>(
                              36
              27                              58
      16                              53              64
                                  40
                                    46
)""")

    def test_remove_not_exist(self):
        bst = gen_binary_search_tree()
        r = bst.remove(1)
        self.assertFalse(r)

    def test_maximum(self):
        bst = gen_binary_search_tree()
        self.assertEqual(bst.maximum.key, 69)

    def test_minimum(self):
        bst = gen_binary_search_tree()
        self.assertEqual(bst.minimum.key, 16)


if __name__ == '__main__':
    unittest.main()
