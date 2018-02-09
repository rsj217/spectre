#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def bubble_opm_sort(lst):
    is_sorted = False
    for i in range(len(lst) - 1):
        if not is_sorted:
            is_sorted = True
            for j in range(len(lst) - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    is_sorted = False
    return lst


def bubble_opm_sort_while(lst):
    i = 0
    is_sorted = False
    while i < len(lst) - 1 and not is_sorted:
        is_sorted = True
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                is_sorted = False
        i += 1
    return lst

if __name__ == '__main__':
    pass
