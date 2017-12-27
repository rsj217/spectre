#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from tree.node import BinNode
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


class TestTreeGen(unittest.TestCase):

    def setUp(self):
        self.bt = BinaryTree()

    def test_empty_tree(self):
        self.assertEqual(self.bt.root, None, msg='空树没有一个节点')
        self.assertEqual(self.bt.stature(self.bt.root), -1, msg="空树的高度为-1")
        self.assertEqual(self.bt.size, 0)
        self.assertEqual(self.bt.is_empty, True)

    def test_insert_root(self):
        root = self.bt.insert_as_root(e='root')
        self.assertEqual(self.bt.root, root)
        self.assertEqual(self.bt.root.data, 'root')
        self.assertEqual(root.height, 0)
        self.assertEqual(root.size, 1)
        self.assertEqual(self.bt.is_empty, False)

    def test_insert_as_left_child_update_height(self):
        root = self.bt.insert_as_root(e='root')
        left = self.bt.insert_as_lc(root, e='left')
        self.assertEqual(root.lchild, left)
        self.assertEqual(left.parent, root)
        self.assertEqual(left.data, 'left')
        self.assertEqual(left.size, 1)
        self.assertEqual(left.height, 0)

        self.assertEqual(root.height, 1)

    def test_insert_as_right_child_update_height_parent(self):
        root = self.bt.insert_as_root(e='root')
        left = self.bt.insert_as_lc(root, e='left')
        right = self.bt.insert_as_rc(left, e='right')

        self.assertEqual(root.lchild.rchild, right)
        self.assertEqual(root.height, 2)
        self.assertEqual(root.size, 3)
        self.assertEqual(left.height, 1)

        self.assertEqual(right.parent, left)
        self.assertEqual(right.parent.parent, root)
        self.assertEqual(right.parent.parent.parent, None)

        right = self.bt.insert_as_rc(root, e='right')
        self.assertEqual(root.rchild, right)
        self.assertEqual(root.height, 2)

    def test_height_and_succ(self):
        """
        <BinaryTree>(

                       i

               d               l

           c       h       k       n

         a       f       j       m   p

          b     e g                 o
        )
        """

        bt = self.bt
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
        self.assertEqual(root.height, 4)
        self.assertEqual(d.height, 3)
        self.assertEqual(l.height, 3)

        self.assertEqual(c.height, 2)
        self.assertEqual(h.height, 2)
        self.assertEqual(k.height, 1)
        self.assertEqual(n.height, 2)

        self.assertEqual(a.height, 1)
        self.assertEqual(f.height, 1)
        self.assertEqual(j.height, 0)
        self.assertEqual(m.height, 0)
        self.assertEqual(p.height, 1)

        self.assertEqual(b.height, 0)
        self.assertEqual(e.height, 0)
        self.assertEqual(g.height, 0)
        self.assertEqual(o.height, 0)

        self.assertEqual(root.succ.data, 'j')
        self.assertEqual(k.succ.data, 'l')
        self.assertEqual(b.succ.data, 'c')

        self.assertEqual(a.deep, 3)
        self.assertEqual(b.deep, 4)


class TestTravel(unittest.TestCase):

    def setUp(self):
        self.bt = gen_binary_tree()
        self.preorder = ['i', 'd', 'c', 'a', 'b', 'h', 'f', 'e', 'g', 'l', 'k', 'j', 'n', 'm', 'p', 'o']
        self.inorder = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
        self.postorder = ['b', 'a', 'c', 'e', 'g', 'f', 'h', 'd', 'j', 'k', 'm', 'o', 'p', 'n', 'l', 'i']
        self.levelorder = ['i', 'd', 'l', 'c', 'h', 'k', 'n', 'a', 'f', 'j', 'm', 'p', 'b', 'e', 'g', 'o']

    # 迭代版遍历
    def test_trav_inorder(self):
        g = self.bt.trav_inorder(self.bt.root)
        ret = [i.data for i in g]
        self.assertEqual(self.inorder, ret)

    def test_trav_postorder(self):
        g = self.bt.trav_postorder(self.bt.root)
        ret = [i.data for i in g]
        self.assertEqual(self.postorder, ret)

    def test_trav_levelorder(self):
        g = self.bt.trav_levelorder(self.bt.root)
        ret = [i.data for i in g]
        self.assertEqual(self.levelorder, ret)

    # 递归版遍历
    def test_preorder(self):
        g = self.bt.preorder(self.bt.root)
        ret = [i.data for i in g]
        self.assertEqual(self.preorder, ret)

    def test_inorder(self):
        g = self.bt.inorder(self.bt.root)
        ret = [i.data for i in g]
        self.assertEqual(self.inorder, ret)

    def test_postorder(self):
        g = self.bt.postorder(self.bt.root)
        ret = [i.data for i in g]
        self.assertEqual(self.postorder, ret)

    def test_trave_pre(self):
        g = self.bt.trave_pre(self.bt.root)
        ret = [i.data for i in g]
        self.assertEqual(self.preorder, ret)

    def test_trave_pre1(self):
        g = self.bt.trave_pre1(self.bt.root)
        ret = [i.data for i in g]
        self.assertEqual(self.preorder, ret)

    def test_trave_pre2(self):
        g = self.bt.trave_pre2(self.bt.root)
        ret = [i.data for i in g]
        self.assertEqual(self.preorder, ret)


if __name__ == '__main__':
    unittest.main()
