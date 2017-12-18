#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tree.node import BSNode
from tree.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):

    def __init__(self, root=None):
        super(BinarySearchTree, self).__init__(root=root)
        self.hot = None

    def search(self, e):
        return self._search_in(self.root, e, hot=None)

    def _search_in(self, node, e, hot):
        if node is None or node.key == e:
            return node
        self.hot = node
        if node.key < e:
            node = node.rchild
        else:
            node = node.lchild
        return self._search_in(node, e, hot=self.hot)

    def find(self, e):
        node = self
        while True or node:
            if e < node.key:
                node = node.lchild
            elif e > node.key:
                node = node.rchild
            else:
                return node

    def insert_as_root(self, e):
        self._size = 1
        self._root = BSNode(key=e)
        return self._root

    def insert(self, e):
        node = self.search(e)
        if not node:
            node = BSNode(parent=self.hot, key=e)
            if node.key < self.hot.key:
                self.hot.lchild = node
            else:
                self.hot.rchild = node
            self._size += 1
            self.update_height_above(self.hot)
        return node


def gen_binary_search_tree():
    bst = BinarySearchTree()
    bst.insert_as_root(36)

    bst.insert(27)
    bst.insert(6)

    return bst


if __name__ == '__main__':
    bst = gen_binary_search_tree()
    print(bst.root, bst.root.lchild, bst.root.lchild.lchild)

