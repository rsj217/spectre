#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'


def insert_sort(lst):
    for i in range(1, len(lst)):
        for j in range(i - 1, -1, -1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == '__main__':
    lst = [1, 2, 4, 6, 3]
    print(insert_sort(lst))
