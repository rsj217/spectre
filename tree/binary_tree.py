#!/usr/bin/env python
# -*- coding:utf-8 -*-


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
        node.height = 1 + max(BinaryTree.stature(node.lchild.height), BinaryTree.stature(node.rchild.height))

    def update_height_above(self, node):
        while node:
            self.update_height(node=node)
            node = node.parent

    def insert_as_rc(self, node, e):
        self._size += 1
        node.insert_as_rc(e)
        self.update_height_above(node=node)
        return node.rchild
