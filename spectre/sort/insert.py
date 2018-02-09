#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'


def insert_sort(lst):
    for i in range(1, len(lst)):
        for j in range(i - 1, -1, -1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def insert_sort_while(lst):
    i = 1
    while i < len(lst):
        j = i - 1
        while j >= 0:
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j -= 1
        i += 1
    return lst


if __name__ == '__main__':
    lst = [1, 1, 4, 6, 3, 0]
    print(insert_sort_while(lst))
