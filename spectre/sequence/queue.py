#!/usr/bin/env python
# -*- coding:utf-8 -*-

from spectre.sequence.list import List


class Queue(List):

    @property
    def front(self):
        return self.first.data

    def enqueue(self, e):
        return self.insert_as_last(e)

    def dequeue(self):
        assert self.size > 0, 'index error'
        node = self.remove(self.first)
        return node.data
