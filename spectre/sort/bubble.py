#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'


def bubble_sort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def opm_sort(l):
    is_sorted = False
    for i in range(len(l) - 1):
        if not is_sorted:
            is_sorted = True
            for j in range(len(l) - i - 1):
                if l[j] > l[j + 1]:
                    l[j], l[j + 1] = l[j + 1], l[j]
                    is_sorted = False
    return l


def opm_sort_other(l):
    i = 0
    is_sorted = False
    while i < len(l) - 1 and not is_sorted:
        is_sorted = True
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                is_sorted = False
        i += 1
    return l

if __name__ == '__main__':
    pass
