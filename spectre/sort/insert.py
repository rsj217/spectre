#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'master'


def insert_sort(lst):
    for i in range(1, len(lst)):
        for j in range(i - 1, -1, -1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# def insert_sort_while(lst):
#     i = 1
#     while i < len(lst):
#         j = i - 1
#         while j >= 0:
#             if lst[j] > lst[j + 1]:
#                 lst[j], lst[j + 1] = lst[j + 1], lst[j]
#             j -= 1
#         i += 1
#     return lst


def insert_sort_while(lst):
    i = 1
    while i < len(lst):
        j = i - 1
        while j >= 0 and lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j -= 1
        i += 1
    return lst


def insert_opm_sort(lst):
    for i in range(1, len(lst)):
        cur_item = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > cur_item:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = cur_item
    return lst


if __name__ == '__main__':
    lst = [0, 2, 6]
    print(insert_opm_sort(lst))
