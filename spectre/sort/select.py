#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'


def select_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[min_index], lst[i] = lst[i], lst[min_index]
    return lst


def select_sort_while(lst):
    i = 0
    while i < len(lst):
        min_index, j = i, i
        while j < len(lst):
            if lst[j] < lst[min_index]:
                min_index = j
            j += 1
        lst[min_index], lst[i] = lst[i], lst[min_index]
        i += 1
    return lst


def find_min_index(lst):
    def _find_min_index(lst, i, min_index):
        if i >= len(lst):
            return min_index

        if lst[i] < lst[min_index]:
            min_index = i
        return _find_min_index(lst, i + 1, min_index)

    return _find_min_index(lst, 0, 0)


def select_recursive_sort(lst):
    def _select_recursive_sort(lst, i):
        if i >= len(lst):
            return lst
        lst_ = lst[i:]
        min_index = find_min_index(lst_)
        lst[i], lst[i + min_index] = lst[i + min_index], lst[i]
        return _select_recursive_sort(lst, i + 1)

    return _select_recursive_sort(lst, 0)


def select_max_sort(lst):
    for i in range(len(lst)):
        max_index = 0
        for j in range(len(lst) - i):
            if lst[max_index] < lst[j]:
                max_index = j
        lst[max_index], lst[len(lst) - i - 1] = lst[len(lst) - i - 1], lst[max_index]
    return lst


if __name__ == '__main__':
    lst = [2, 1, 1, 10]
    print(select_recursive_sort(lst))
