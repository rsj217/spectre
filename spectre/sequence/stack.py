#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'

from spectre.sequence.vector import Vector


class Stack(Vector):

    @property
    def top(self):
        return self._elem[self._size - 1]

    def push(self, e):
        return self.insert(self.size, e)

    def pop(self):
        return self.remove(self.size - 1)
