#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tree.binary_search_tree import BinarySearchTree


class BalanceBinarySearchTree(BinarySearchTree):

    def bal_fac(self, node):
        return self.stature(node.lchild) - self.stature(node.rchild)

    def balanced(self, node):
        return self.stature(node.lchild) == self.stature(node.rchild)

    def left_rotate(self):
        pass

    def right_rotate(self):
        pass


class AVLTree(BalanceBinarySearchTree):

    def avl_balanced(self, node):
        return abs(self.bal_fac(node) >= 1)


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