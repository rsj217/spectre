#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import random
import unittest
from spectre.sort.bubble import bubble_sort, opm_sort, opm_sort_other
from spectre.sort.select import select_sort, select_max_sort

now = lambda: time.time()


def gen_random_lst(n, l, r):
    lst = [random.randint(l, r) for i in range(n)]
    # print('random list {}'.format(lst[:30]))
    return lst


def gen_nearly_order_list(n, s):
    lst = list(range(n))
    for i in range(s):
        x = random.randint(0, n)
        y = random.randint(0, n)
        lst[x], lst[y] = lst[y], lst[x]
    # print('nearly order list {}'.format(lst[:30]))
    return lst


def test_random_helper(func, n, l, r):
    lst = gen_random_lst(n, l, r)
    sorted_lst = lst.copy()
    sorted_lst.sort()
    start = now()
    lst = func(lst)
    ret = True if lst == sorted_lst else False
    print("{} - {} - {} s".format(func.__name__.upper(), ret, now() - start))
    return ret


def test_nearly_order_helper(func, l, s):
    lst = gen_nearly_order_list(l, s)
    sorted_lst = lst.copy()
    sorted_lst.sort()
    start = now()
    lst = func(lst)
    ret = True if lst == sorted_lst else False
    print("{} - {} - {} s".format(func.__name__.upper(), ret, now() - start))
    return ret


class TestBubbleSort(unittest.TestCase):

    def test_common_sort(self):
        print('RANDOM')
        ret = test_random_helper(bubble_sort, 1000, 0, 1000)
        self.assertTrue(ret)

        print('REPEAT')
        ret = test_random_helper(bubble_sort, 1000, 0, 10)
        self.assertTrue(ret)

        print('NEARLY ORDER')
        ret = test_nearly_order_helper(bubble_sort, 1000, 10)
        self.assertTrue(ret)

    def test_opm_sort(self):
        print('RANDOM')
        ret = test_random_helper(opm_sort, 1000, 0, 1000)
        self.assertTrue(ret)

        print('REPEAT')
        ret = test_random_helper(opm_sort, 1000, 0, 10)
        self.assertTrue(ret)

        print('NEARLY ORDER')
        ret = test_nearly_order_helper(opm_sort, 1000, 10)
        self.assertTrue(ret)

    def test_opm_sort_other(self):
        print('RANDOM')
        ret = test_random_helper(opm_sort_other, 1000, 0, 1000)
        self.assertTrue(ret)

        print('REPEAT')
        ret = test_random_helper(opm_sort_other, 1000, 0, 10)
        self.assertTrue(ret)

        print('NEARLY ORDER')
        ret = test_nearly_order_helper(opm_sort_other, 1000, 10)
        self.assertTrue(ret)


class TestSelectSort(unittest.TestCase):

    def test_select_sort(self):
        print('RANDOM')
        ret = test_random_helper(select_sort, 1000, 0, 1000)
        self.assertTrue(ret)

        print('REPEAT')
        ret = test_random_helper(select_sort, 1000, 0, 10)
        self.assertTrue(ret)

        print('NEARLY ORDER')
        ret = test_nearly_order_helper(select_sort, 1000, 10)
        self.assertTrue(ret)

    def test_select_max_sort(self):
        print('RANDOM')
        ret = test_random_helper(select_max_sort, 1000, 0, 1000)
        self.assertTrue(ret)

        print('REPEAT')
        ret = test_random_helper(select_max_sort, 1000, 0, 10)
        self.assertTrue(ret)

        print('NEARLY ORDER')
        ret = test_nearly_order_helper(select_max_sort, 1000, 10)
        self.assertTrue(ret)


class TestSortSpeed(unittest.TestCase):

    def test_random(self):
        print('RANDOM --- ')
        ret = test_random_helper(opm_sort, 2000, 0, 2000)
        self.assertTrue(ret)

        ret = test_random_helper(select_sort, 2000, 0, 2000)
        self.assertTrue(ret)

    def test_repeat(self):
        print('REPEAT --- ')
        ret = test_random_helper(opm_sort, 1000, 0, 10)
        self.assertTrue(ret)

        print('REPEAT')
        ret = test_random_helper(select_sort, 1000, 0, 10)
        self.assertTrue(ret)

    def test_nearly_order(self):
        print('NEARLY ORDER ---')
        ret = test_nearly_order_helper(opm_sort, 1000, 10)
        self.assertTrue(ret)

        print('NEARLY ORDER')
        ret = test_nearly_order_helper(select_sort, 1000, 10)
        self.assertTrue(ret)


if __name__ == '__main__':
    unittest.main()
