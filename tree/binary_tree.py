#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tree.node import BinNode


class BinaryTree(object):

    def __init__(self, root=None):
        self._root = root
        self._size = 0

    @property
    def size(self):
        return self._size

    @property
    def is_empty(self):
        return self.root is None

    @property
    def root(self):
        return self._root

    @staticmethod
    def stature(p):
        if p:
            return p.height
        return -1

    @staticmethod
    def update_height(node):
        lheight = BinaryTree.stature(node.lchild) if node.lchild else 0
        rheight = BinaryTree.stature(node.rchild) if node.rchild else 0
        node.height = 1 + max(lheight, rheight)
        return node.height

    def update_height_above(self, node):
        while node:
            old_height = node.height
            new_height = self.update_height(node=node)
            if old_height == new_height:
                break
            node = node.parent

    def insert_as_root(self, e):
        self._size = 1
        self._root = BinNode(data=e)
        return self._root

    def insert_as_lc(self, node, e):
        self._size += 1
        node.insert_as_lc(e)
        self.update_height_above(node)
        return node.lchild

    def insert_as_rc(self, node, e):
        self._size += 1
        node.insert_as_rc(e)
        self.update_height_above(node=node)
        return node.rchild

    def trave_pre(self):
        stack = []
        stack.append(self.root)
        while stack:
            node = stack.pop()
            yield node.data
            if node.rchild:
                stack.append(node.rchild)
            if node.lchild:
                stack.append(node.lchild)

    def trave_pre1(self):
        stack = []
        node = self.root
        while stack or node:
            if node:
                yield node.data
                stack.append(node)
                node = node.lchild
            else:
                node = stack.pop()
                node = node.rchild

    def trave_pre2(self):
        stack = []
        node = self.root
        need = True
        while True:
            if need:
                while node:
                    yield node.data
                    stack.append(node)
                    node = node.lchild

            if not stack:
                break
            node = stack.pop()
            if node.rchild:
                need = True
                node = node.rchild
            else:
                need = False

    def trave_pre3(self):
        stack = []
        node = self.root
        while True:
            while node:
                yield node.data
                stack.append(node)
                node = node.lchild

            if not stack:
                break
            node = stack.pop()
            node = node.rchild

    def trave_pre4(self):
        stack = []
        node = self.root
        while True:
            while node:
                yield node.data
                if node.rchild:
                    stack.append(node.rchild)
                node = node.lchild
            if not stack:
                break
            node = stack.pop()

    def visit_along_left_branch(self, stack, node):
        while node:
            yield node.data
            if node.rchild:
                stack.append(node.rchild)
            node = node.lchild

    def trave_pre_along_left_branch(self):
        stack = []
        node = self.root
        while True:
            g = self.visit_along_left_branch(stack, node)
            for i in g:
                yield i
            if not stack:
                break
            node = stack.pop()

    def preorder(self):
        self._preorder(self._root)

    def inorder(self):
        self._inorder(self._root)

    def trave_in(self):
        stack = []
        node = self.root
        while True:
            while node:
                stack.append(node)
                node = node.lchild

            if not stack:
                break
            node = stack.pop()
            yield node.data
            node = node.rchild

    def trave_in2(self):
        stack = []
        node = self.root
        while stack or node:
            if node:
                stack.append(node)
                node = node.lchild
            else:
                node = stack.pop()
                yield node.data
                node = node.rchild

    def trave_in3(self):
        stack = []
        node = self.root
        while True:
            if node:
                stack.append(node)
                node = node.lchild
            elif not stack:
                break
            else:
                node = stack.pop()
                yield node.data
                node = node.rchild

    def trave_post(self):
        stack = []
        node = self.root
        rchild = None
        while True:
            while node:
                stack.append(node)
                node = node.lchild
            if not stack:
                break
            if stack[-1].rchild != rchild:
                node = stack[-1].rchild
                rchild = None
            else:
                rchild = stack.pop()
                yield rchild.data

    def trave_post2(self):
        stack = []
        node = self.root
        rchild = None
        while stack or node:
            if node:
                stack.append(node)
                node = node.lchild
            elif stack[-1].rchild is not rchild:
                node = stack[-1].rchild
                rchild = None
            else:
                rchild = stack.pop()
                yield rchild.data

    def trave_post3(self):
        stack = []
        node = self.root
        rchild = None
        while True:
            if node:
                stack.append(node)
                node = node.lchild
            elif not stack:
                break
            elif stack[-1].rchild != rchild:
                node = stack[-1].rchild
                rchild = None
            else:
                rchild = stack.pop()
                yield rchild.data

    def trave_level(self):
        queue = []
        node = self.root
        queue.append(node)
        while queue:
            node = queue.pop(0)
            yield node
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    def postorder(self):
        self._postorder(self._root)

    def _preorder(self, node):
        if not node:
            return
        print(node.data)
        self._preorder(node.lchild)
        self._preorder(node.rchild)

    def _inorder(self, node):
        if not node:
            return
        self._inorder(node.lchild)
        print(node.data)
        self._inorder(node.rchild)

    def _postorder(self, node):
        if not node:
            return
        self._postorder(node.lchild)
        self._postorder(node.rchild)
        print(node.data)


def gen_binary_tree():
    bt = BinaryTree()
    root = bt.insert_as_root('i')
    d = bt.insert_as_lc(root, 'd')
    c = bt.insert_as_lc(d, 'c')
    a = bt.insert_as_lc(c, 'a')
    b = bt.insert_as_rc(a, 'b')
    h = bt.insert_as_rc(d, 'h')
    f = bt.insert_as_lc(h, 'f')
    e = bt.insert_as_lc(f, 'e')
    g = bt.insert_as_rc(f, 'g')

    l = bt.insert_as_rc(root, 'l')
    k = bt.insert_as_lc(l, 'k')
    j = bt.insert_as_lc(k, 'j')
    n = bt.insert_as_rc(l, 'n')
    m = bt.insert_as_lc(n, 'm')
    p = bt.insert_as_rc(n, 'p')
    o = bt.insert_as_lc(p, 'o')
    #
    # for item in [a, b, c, d, e, f, g, h, root, j, k, l, m, n, o, p]:
    #     print(item.data, item.succ)
    #
    # print(p.data, p.succ)

    return bt


if __name__ == '__main__':
    bt = gen_binary_tree()
    g = bt.trave_in3()
    for i in g:
        print(i)
