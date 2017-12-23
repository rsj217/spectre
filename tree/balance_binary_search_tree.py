#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tree.binary_search_tree import BinarySearchTree


class BalanceBinarySearchTree(BinarySearchTree):

    def bal_fac(self, node):
        return self.stature(node.lchild) - self.stature(node.rchild)

    def balanced(self, node):
        return self.stature(node.lchild) == self.stature(node.rchild)

    def taller_child(self, node):
        if self.stature(node.lchild) > self.stature(node.rchild):
            return node.lchild

        elif self.stature(node.lchild) > self.stature(node.rchild):
            return node.rchild
        else:
            if node == node.parent.lchild:
                return node.lchild
            else:
                return node.rchild

    def zig_rotate(self, node):
        pass

    def right_rotate(self):
        pass


class AVLTree(BalanceBinarySearchTree):

    def avl_balanced(self, node):
        return abs(self.bal_fac(node) >= 1)


def gen_avl_tree():
    """
    <AVLTree>(
          58
      53      69
    40  54
    )
    """
    avl = AVLTree()
    avl.insert_as_root(58)

    avl.insert(53)
    avl.insert(40)
    avl.insert(69)
    avl.insert(54)

    return avl


if __name__ == '__main__':
    avl = gen_avl_tree()
    x = avl.insert(30)
    while x:
        print(avl.bal_fac(x))
        x = x.parent
