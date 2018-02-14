#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from spectre.tree.node import Entry
from spectre.tree.balance_binary_search_tree import AVLTree


def gen_tree():
    n58 = Entry(key=58, value=58)
    avl = AVLTree()
    avl.insert_as_root(n58)

    n53 = Entry(key=53, value=53)
    n40 = Entry(key=40, value=40)
    n69 = Entry(key=69, value=69)
    n54 = Entry(key=54, value=54)

    avl.insert(n53)
    avl.insert(n40)
    avl.insert(n69)
    avl.insert(n54)
    return avl


def gen_avl_tree():
    n50 = Entry(key=50, value=50)
    n30 = Entry(key=30, value=30)
    n58 = Entry(key=58, value=58)
    n20 = Entry(key=20, value=20)
    n54 = Entry(key=54, value=54)
    n69 = Entry(key=69, value=69)
    n52 = Entry(key=52, value=52)

    avl = AVLTree()
    avl.insert_as_root(n50)

    avl.insert(n30)
    avl.insert(n58)
    avl.insert(n20)
    avl.insert(n54)
    avl.insert(n69)
    avl.insert(n52)
    return avl


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
        avl = gen_tree()
        print(avl)
        g = avl.trav_levelorder(avl.root)
        for i in g:
            self.assertTrue(avl.avl_balanced(i))

    def test_remove_zig_zig(self):
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
        avl = gen_avl_tree()
        avl.remove(69)
        print(avl)
        g = avl.trav_levelorder(avl.root)
        for i in g:
            self.assertTrue(avl.avl_balanced(i))

    def test_remove_zag_zig(self):
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
        avl = gen_avl_tree()
        avl.remove(30)
        print(avl)
        g = avl.trav_levelorder(avl.root)
        for i in g:
            self.assertTrue(avl.avl_balanced(i))

    def test_remove_zig_zag(self):

        avl = gen_avl_tree()
        e25 = Entry(key=25, value=25)
        avl.insert(e25)
        avl.remove(50)
        print(avl)
        g = avl.trav_levelorder(avl.root)
        for i in g:
            self.assertTrue(avl.avl_balanced(i))


    def test_remove_zag_zag(self):

        avl = gen_avl_tree()
        e21 = Entry(key=21, value=21)
        e22 = Entry(key=35, value=22)
        avl.insert(e21)
        avl.insert(e22)
        print(avl)
        avl.remove(20)
        print(avl)
        g = avl.trav_levelorder(avl.root)
        for i in g:
            self.assertTrue(avl.avl_balanced(i))



if __name__ == '__main__':
    unittest.main()
