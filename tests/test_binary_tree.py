#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from tree.node import BSNode
from tree.binary_tree import BinaryTree


def gen_binary_tree():
    """
    <BinaryTree>(
                   i
           d               l
       c       h       k       n
     a       f       j       m   p
      b     e g                 o
    )
    """
    bt = BinaryTree()
    root = bt.insert_as_root('i')
    d = bt.insert_as_lc(root, 'd')
    c = bt.insert_as_lc(d, 'c')
    a = bt.insert_as_lc(c, 'a')
    b = bt.insert_as_rc(a, 'b')
    h = bt.insert_as_rc(d, 'h')
    f = bt.insert_as_lc(h, 'f')
    e = bt.insert_as_lc(f, 'e')
    g = bt.insert_as_rc(f, 'g')

    l = bt.insert_as_rc(root, 'l')
    k = bt.insert_as_lc(l, 'k')
    j = bt.insert_as_lc(k, 'j')
    n = bt.insert_as_rc(l, 'n')
    m = bt.insert_as_lc(n, 'm')
    p = bt.insert_as_rc(n, 'p')
    o = bt.insert_as_lc(p, 'o')

    return bt


class TestTree(unittest.TestCase):

    def setUp(self):
        self.bt = BinaryTree()

    def test_empty_tree(self):
        pass

    def test_insert_root(self):
        pass

    def test_tree_node(self):
        pass


if __name__ == '__main__':
    unittest.main()
