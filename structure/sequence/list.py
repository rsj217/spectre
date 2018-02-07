#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Node(object):

    def __init__(self, data=None, pred=None, succ=None):
        self._data = data
        self._pred = pred
        self._succ = succ

    def __repr__(self):
        return '<Node>({})'.format(self._data)

    @property
    def pred(self):
        return self._pred

    @property
    def succ(self):
        return self._succ

    def insert_as_pred(self, e):
        node = Node(data=e, pred=self._pred, succ=self)
        self._pred._succ = node
        self._pred = node
        return node

    def insert_as_succ(self, e):
        node = Node(data=e, pred=self, succ=self._succ)
        self._succ = node
        self._succ._pred = node
        return node


class List(object):

    def __init__(self):
        self._header = Node()
        self._trailer = Node()
        self._header._succ = self._trailer
        self._trailer._pred = self._header
        self._size = 0

    def __repr__(self):
        return '<List>({})'.format(self._size)

    def __getitem__(self, r):
        assert r < self._size, 'index error'
        p = self.first
        for i in range(r):
            p = p.succ
        return p

    @property
    def size(self):
        return self._size

    @property
    def first(self):
        return self._header.succ

    @property
    def last(self):
        return self._trailer.pred

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


if __name__ == '__main__':
    n = Node(123)
    l = List()
    print(n, l)
    print(l[-1])
