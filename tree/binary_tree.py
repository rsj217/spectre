#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tree.node import BinNode


class BinaryTree(object):

    def __init__(self, root=None):
        self._root = root
        self._size = 0

    @property
    def size(self):
        return self._size

    @property
    def is_empty(self):
        return self.root is None

    @property
    def root(self):
        return self._root

    @staticmethod
    def stature(p):
        if p:
            return p.height
        return -1

    @staticmethod
    def update_height(node):
        lheight = BinaryTree.stature(node.lchild) if node.lchild else 0
        rheight = BinaryTree.stature(node.rchild) if node.rchild else 0
        node.height = 1 + max(lheight, rheight)
        return node.height

    def update_height_above(self, node):
        while node:
            old_height = node.height
            new_height = self.update_height(node=node)
            if old_height == new_height:
                break
            node = node.parent

    def insert_as_root(self, e):
        self._size = 1
        root = BinNode(data=e)
        return root

    def insert_as_lc(self, node, e):
        self._size += 1
        node.insert_as_lc(e)
        self.update_height_above(node)
        return node.lchild

    def insert_as_rc(self, node, e):
        self._size += 1
        node.insert_as_rc(e)
        self.update_height_above(node=node)
        return node.rchild

    def preorder(self, node):
        if node:
            return
        yield node.data
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        if node:
            return
        self.inorder(node.lchild)
        yield node.data
        self.inorder(node.rchild)

    def postorder(self, node):
        if node:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        yield node


def gen_binary_tree():
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
    p = bt.insert_as_rc(n, 'p')
    o = bt.insert_as_lc(p, 'o')

    print(root)
    print(d), print(l)
    print(c), print(h)
    print(a), print(b)

    print(f)

    print(e), print(g)
    print(k), print(n)
    print(j), print(p), print(o)

if __name__ == '__main__':
    gen_binary_tree()
