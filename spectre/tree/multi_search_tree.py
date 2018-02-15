#!/usr/bin/env python
# -*- coding:utf-8 -*-


class BTree(object):

    def __init__(self, order=3):
        self._size = 0
        self._order = order
        self._root = None
        self._hot = None

    @property
    def size(self):
        return self._size

    @property
    def order(self):
        return self._order

    @property
    def root(self):
        return self._root

    @property
    def empty(self):
        return not self._root

    def search(self):
        pass

    def insert(self):
        pass

    def remove(self):
        pass

    def solve_overflow(self):
        pass

    def solve_underflow(self):
        pass
