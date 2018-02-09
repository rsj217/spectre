#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'


def select_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i, len(l)):
            if l[min_index] > l[j]:
                min_index = j
        l[min_index], l[i] = l[i], l[min_index]
    return l


if __name__ == '__main__':
    l = [2, 1, 3, 4, 10]
    print(select_sort(l))
