#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'

import ctypes


class Vector(object):

    def __init__(self, size=0, capacity=0):
        self._size = size
        self._capacity = capacity
        self._elem = self.__make_elem(size, capacity)

    def __getitem__(self, item):
        return self._elem[item]

    def __setitem__(self, key, value):
        assert key < self._size, 'index error'
        self._elem[key] = value

    def __iter__(self):
        for i in range(self._size):
            yield self._elem[i]

    def __repr__(self):
        return '<Vector>({})'.format([self._elem[e] for e in range(self._size)])

    def __len__(self):
        return self._size

    def __make_elem(self, size, capacity):
        elem = (capacity * ctypes.py_object)()
        for i in range(size):
            elem[i] = 0
        return elem

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

    def expand(self):
        if self._size < self._capacity:
            return
        new_capacity = 2 * self._capacity
        _elem = (new_capacity * ctypes.py_object)()
        for index, i in enumerate(self._elem):
            _elem[index] = i
        self._elem = _elem
        self._capacity = new_capacity

    def find(self, e, lo=0, hi=None):
        if hi is None:
            hi = self._size

        while lo < hi:
            if self._elem[lo] == e:
                return lo
            lo += 1
        return -1

    def search(self, e):
        """ 有序查找 """
        pass

    def remove(self, r):
        assert r < self.size, 'index error'
        e = self._elem[r]
        self.remove_range(r, r + 1)
        return e

    def remove_range(self, lo, hi):
        assert lo >= 0, 'index error'
        assert hi <= self.size, 'index error'

        count = hi - lo
        size = self._size
        for i in range(hi, size):
            self._elem[lo] = self._elem[i]
            # self._elem[i] = None
            lo += 1

        self._size -= count
        return count

    def insert(self, r, e):
        if self._size >= self._capacity:
            self.expand()

        for i in range(self._size, r, -1):
            self._elem[i] = self._elem[i - 1]
        self._elem[r] = e
        self._size += 1

    def deduplicate(self):
        """ 无序向量唯一化 """
        old_size = self._size
        i = 1
        while i < self._size:
            if self.find(self[i], 0, i) < 0:
                i += 1
            else:
                self.remove(i)
        return old_size - self._size

    def low_uniquify(self):
        """ 有序向量唯一化 低效版"""
        old_size = self._size
        i = 0

        while i < self._size - 1:
            if self[i] == self[i + 1]:
                self.remove(i + 1)
            else:
                i += 1

        return old_size - self._size

    def uniquify(self):
        """ 有序向量唯一化 """
        i, j = 0, 1
        while j < self._size:
            if self[i] != self[j]:
                self[i + 1] = self[j]
                i += 1
            j += 1
        i += 1
        self._size = i
        return j - i

    def disordered(self):
        n = 0
        for i in range(1, self._size):
            if self[i - 1] > self[i]:
                n += 1
        return n


if __name__ == '__main__':
    pass
