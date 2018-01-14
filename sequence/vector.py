#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'


class Vector(object):

    def __init__(self, size=0, capacity=0, value=0):
        self._size = size
        self._capacity = capacity
        self._elem = self.init_elem(size, capacity, value)

    def init_elem(self, size, capacity, value):
        elem = [value for i in range(size)]
        elem.extend([None for i in range(capacity - size)])
        return elem

    def __getitem__(self, item):
        return self._elem[item]

    def __setitem__(self, key, value):
        assert key < self._size, 'index error'
        self._elem[key] = value

    @property
    def size(self):
        return self._size

    @property
    def data(self):
        return self._elem[0:self._size]

    @property
    def cap(self):
        return self._capacity

    @property
    def empty(self):
        return self._size == 0

    def copy_form(self, V, lo, hi):
        _capacity = 2 * (hi - lo)
        _size = 0
        _elem = [None for i in range(_capacity)]
        while lo < hi:
            _elem[_size] = V[lo]
            _size += 1
            lo += 1

    def expand(self):
        if self._size < self._capacity:
            return

        old_elem = self._elem
        new_capacity = 2 * self._capacity
        _elem = [None for i in range(new_capacity)]
        for index, i in enumerate(old_elem):
            _elem[index] = old_elem[index]
        del old_elem
        self._elem = _elem
        self._capacity = new_capacity

    def find(self, e):
        """ 无序查找 """
        pass

    def search(self, e):
        """ 有序查找 """
        pass

    def remove(self, r):
        assert r < self.size, 'index error'
        return self.remove_(r, r + 1)

    def remove_(self, lo, hi):
        assert lo >= 0, 'index error'
        assert hi <= self.size, 'index error'

        e = self._elem[lo]
        count = hi - lo
        size = self._size
        for i in range(hi, size):
            self._elem[lo] = self._elem[i]
            self._elem[i] = None
            lo += 1

        self._size -= count
        return e

    def insert(self, r, e):
        if self._size >= self._capacity:
            self.expand()

        for i in range(self._size, r, -1):
            self._elem[i] = self._elem[i - 1]
        self._elem[r] = e
        self._size += 1

    def append(self, e):
        """ 追加 """

    def sort(self):
        """ 整体排序 """

    def unsort(self):
        """ 整体置乱 """

    def deduplicate(self):
        """  """

    def __repr__(self):
        return '<Vector>({})'.format([e for e in self._elem if e is not None])

    def __len__(self):
        return self._size


if __name__ == '__main__':
    pass
