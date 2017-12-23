#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tree.binary_search_tree import BinarySearchTree


class BalanceBinarySearchTree(BinarySearchTree):

    def bal_fac(self, node):
        return self.stature(node.lchild) - self.stature(node.rchild)

    def balanced(self, node):
        return self.stature(node.lchild) == self.stature(node.rchild)

    def zig_rotate(self, node):
        p = node.parent
        c = node.lchild

        if p:
            if node is p.lchild:
                p.lchild = node
            else:
                p.rchild = node
            node.parent = c
        c.parent = p

        node.lchild = c.rchild
        if c.rchild:
            c.rchild.parent = node

        c.rchild = node
        node.parent = c

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
    avl.insert_as_root(58)

    avl.insert(53)
    avl.insert(40)
    avl.insert(69)
    avl.insert(54)

    return avl


if __name__ == '__main__':
    avl = gen_avl_tree()
    print(avl)
    avl.inorder()

    avl.zig_rotate(avl.root)

    # print(avl)

    avl.inorder(avl.root.parent)
