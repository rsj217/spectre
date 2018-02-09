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


def insert_sort_opm(lst):
    for i in range(1, len(lst)):
        cur_item = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > cur_item:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = cur_item
    return lst


def insert_item(lst, item):
    if not lst:
        return [item]
    *head, tail = lst
    if item >= tail:
        lst.append(item)
        return lst
    l = insert_item(head, item)
    l.append(tail)
    return l


def insert_sort_recursive(lst):
    if not lst:
        return []
    *head, tail = lst
    return insert_item(insert_sort_recursive(head), tail)


if __name__ == '__main__':
    lst = [1, 2, 5, 2, 3]
    print(insert_sort_recursive(lst))
