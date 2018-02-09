#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'


def select_sort(l):
    for i in range(len(l)):
        min_index = i
        for j in range(i, len(l)):
            if l[j] < l[min_index]:
                min_index = j
        l[min_index], l[i] = l[i], l[min_index]
    return l


def select_sort_while(l):
    i = 0
    while i < len(l):
        min_index, j = i, i
        while j < len(l):
            if l[j] < l[min_index]:
                min_index = j
            j += 1
        l[min_index], l[i] = l[i], l[min_index]
        i += 1
    return l


def select_max_sort(l):
    for i in range(len(l)):
        max_index = 0
        for j in range(len(l) - i):
            if l[max_index] < l[j]:
                max_index = j
        l[max_index], l[len(l) - i - 1] = l[len(l) - i - 1], l[max_index]
    return l


if __name__ == '__main__':
    l = [2, 1, 3, 4, 10]
    print(select_sort_while(l))
