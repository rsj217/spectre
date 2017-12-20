#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tree.binary_search_tree import BinarySearchTree


class BalanceBinarySearchTree(BinarySearchTree):
    pass


class AVLTree(BalanceBinarySearchTree):
    pass


def gen_avl_tree():
    """
    <BinarySearchTree>(
                                  36
                  27                              58
          16                              53              69
                                      40              64
                                        46
    )
    """
    avl = AVLTree()
    avl.insert_as_root(36)

    avl.insert(27)
    avl.insert(16)
    avl.insert(58)
    avl.insert(53)
    avl.insert(40)
    avl.insert(69)
    avl.insert(64)

    return avl


if __name__ == '__main__':
    avl = gen_avl_tree()
    print(avl)
