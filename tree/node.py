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
            s += self.lchild.size()
        if self.rchild:
            s += self.rchild.size()
        return s

    def succ(self):
        pass
