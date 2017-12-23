#!/usr/bin/env python
# -*- coding:utf-8 -*-


class BinNode(object):

    def __init__(self, parent=None, lchild=None, rchild=None, data=None):
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild
        self.data = data
        self.height = 0

    def __repr__(self):
        pdata = getattr(self.parent, 'data', None)
        ldata = getattr(self.lchild, 'data', None)
        rdata = getattr(self.rchild, 'data', None)
        return f'<BinNode>([{pdata}] {ldata}-{self.data}-{rdata}: {self.height})'

    def insert_as_lc(self, e):
        node = BinNode(parent=self, data=e)
        self.lchild = node
        return node

    def insert_as_rc(self, e):
        node = BinNode(parent=self, data=e)
        self.rchild = node
        return node

    @property
    def size(self):
        s = 1
        if self.lchild:
            s += self.lchild.size
        if self.rchild:
            s += self.rchild.size
        return s

    @property
    def succ(self):
        node = self
        if node.rchild:
            node = node.rchild
            while node.lchild:
                node = node.lchild
        else:
            while node.parent and node.parent.rchild == node:
                node = node.parent
            node = node.parent
        return node

    @property
    def precu(self):
        return

    @property
    def deep(self):
        d = -1
        node = self
        while node:
            node = node.parent
            d += 1
        return d


class BSNode(BinNode):

    def __init__(self, key, data=None, parent=None):
        data = data or key
        super(BSNode, self).__init__(parent=parent, lchild=None, rchild=None, data=data)
        self.key = key

    def __repr__(self):
        pdata = getattr(self.parent, 'key', None)
        ldata = getattr(self.lchild, 'key', None)
        rdata = getattr(self.rchild, 'key', None)
        return f'<BSNode>([{pdata}] {ldata}-{self.key}-{rdata}: {self.height})'

    def insert_as_lc(self, e):
        raise NotImplementedError

    def insert_as_rc(self, e):
        raise NotImplementedError
