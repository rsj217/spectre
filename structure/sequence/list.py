#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Node(object):

    def __init__(self, data=None, pred=None, succ=None):
        self._data = data
        self._pred = pred
        self._succ = succ

    def __repr__(self):
        data = self._data
        return '<Node>({})'.format(data)

    @property
    def data(self):
        return self._data

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
        self._succ._pred = node
        self._succ = node
        return node


class List(object):

    def __init__(self):
        self._header = Node()
        self._tailer = Node()
        self._header._succ = self._tailer
        self._tailer._pred = self._header
        self._size = 0

    def __repr__(self):
        data = [self[i].data for i in range(self._size)]
        return '<List>({}-{})'.format(data, self._size)

    def __getitem__(self, r):
        assert r < self._size, 'index error'
        p = self.first
        for i in range(r):
            p = p.succ
        return p

    def __iter__(self):
        p = self.first
        for i in range(self.size):
            yield p.data
            p = p.succ

    @property
    def size(self):
        return self._size

    @property
    def empty(self):
        return self._size == 0

    @property
    def first(self):
        return self._header.succ

    @property
    def last(self):
        return self._tailer.pred

    def insert_as_first(self, e):
        self._size += 1
        return self._header.insert_as_succ(e)

    def insert_as_last(self, e):
        self._size += 1
        return self._tailer.insert_as_pred(e)

    def insert_before(self, node, e):
        self._size += 1
        return node.insert_as_pred(e)

    def insert_after(self, node, e):
        self._size += 1
        return node.insert_as_succ(e)

    def remove(self, node):
        self._size -= 1
        pred = node.pred
        succ = node.succ
        pred._succ = succ
        succ._pred = pred

        node._pred = None
        node._succ = None


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
    l = List()
    f = l.insert_as_first(1)
    print(l)
    l.insert_after(f, 2)
    print(l[0])
    print(l[1])
    print(l)
