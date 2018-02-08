#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'


def sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


if __name__ == '__main__':
    pass
