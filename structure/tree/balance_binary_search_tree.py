#!/usr/bin/env python
# -*- coding:utf-8 -*-

from structure.tree.node import BSNode
from structure.tree.binary_search_tree import BinarySearchTree


class BalanceBinarySearchTree(BinarySearchTree):

    def bal_fac(self, node):
        return self.stature(node.lchild) - self.stature(node.rchild)

    def balanced(self, node):
        return self.stature(node.lchild) == self.stature(node.rchild)

    def taller_child(self, node):
        if self.stature(node.lchild) > self.stature(node.rchild):
            return node.lchild

        elif self.stature(node.lchild) < self.stature(node.rchild):
            return node.rchild
        else:
            return node.lchild if node.is_lchild else node.rchild

    def connect34(self, a, b, c, t0, t1, t2, t3):
        a.lchild = t0
        if t0:
            t0.parent = a
        a.rchild = t1
        if t1:
            t1.parent = a
        self.update_height(a)

        c.lchild = t2
        if t2:
            t2.parent = c
        c.rchild = t3
        if t3:
            t3.parent = c
        self.update_height(c)

        b.lchild, a.parent = a, b
        b.rchild, c.parent = c, b
        self.update_height(b)

        return b


class AVLTree(BalanceBinarySearchTree):

    def avl_balanced(self, node):
        return abs(self.bal_fac(node)) <= 1

    def insert(self, e):
        node = self.search(e)
        if not node:
            node = BSNode(key=e, parent=self.hot)
            if node.key < self.hot.key:
                self.hot.lchild = node
            else:
                self.hot.rchild = node
            self._size += 1

            g = self.hot
            while g:
                if not self.avl_balanced(g):
                    if g.is_root:
                        self._root = self.rotate_at(self.taller_child(self.taller_child(g)))
                    elif g.is_lchild:
                        gg = g.parent
                        gg.lchild = self.rotate_at(self.taller_child(self.taller_child(g)))
                    else:
                        gg = g.parent
                        gg.rchild = self.rotate_at(self.taller_child(self.taller_child(g)))
                    break
                else:
                    self.update_height(g)
                g = g.parent

        return node

    def remove(self, e):
        node = self.search(e)
        if not node:
            return False
        self._remove_at(node)
        self._size -= 1
        g = self.hot
        while g:
            if not self.avl_balanced(g):
                if g.is_root:
                    self._root = self.rotate_at(self.taller_child(self.taller_child(g)))
                elif g.is_lchild:
                    gg = g.parent
                    gg.lchild = self.rotate_at(self.taller_child(self.taller_child(g)))
                else:
                    gg = g.parent
                    gg.rchild = self.rotate_at(self.taller_child(self.taller_child(g)))
            self.update_height(g)
            g = g.parent
        return True

    def rotate_at(self, v):
        p = v.parent
        g = p.parent

        if p.is_lchild:  # zig
            if v.is_lchild:  # zig-zig
                p.parent = g.parent
                return self.connect34(v, p, g, v.lchild, v.rchild, p.rchild, g.rchild)
            else:  # zig-zag
                v.parent = g.parent
                return self.connect34(p, v, g, p.lchild, v.lchild, v.rchild, g.rchild)
        else:  # zag
            if v.is_rchild:  # zag-zag
                p.parent = g.parent
                return self.connect34(g, p, v, g.lchild, p.lchild, v.lchild, v.rchild)
            else:  # zag-zig
                v.parent = g.parent
                return self.connect34(g, v, p, g.lchild, v.lchild, v.rchild, p.rchild)


def gen_avl_tree():
    """
    <AVLTree>(
          53
      40      58
            54  69
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
