#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Node(object):

    def __init__(self, data=None, pred=None, succ=None):
        self._data = data
        self._pred = pred
        self._succ = succ

    @property
    def pred(self):
        return

    @property
    def succ(self):
        return

    def insert_as_pred(self, e):
        pass

    def insert_as_succ(self, e):
        pass


class List(object):

    def __init__(self):
        self._header = Node()
        self._trailer = Node()
        self._header._succ = self._trailer
        self._trailer._pred = self._header
        self._size = 0

    @property
    def size(self):
        return self._size

    @property
    def first(self):
        return ''

    @property
    def last(self):
        return ''

    def insert_as_first(self, e):
        pass

    def insert_as_last(self, e):
        pass

    def insert_before(self, e):
        pass

    def insert_after(self, e):
        pass

    def remove(self):
        pass

    def disordered(self):
        pass

    def sort(self):
        pass

    def find(self, e):
        pass

    def search(self, e):
        pass

    def uniquify(self):
        pass
