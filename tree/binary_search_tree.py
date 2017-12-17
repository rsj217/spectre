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
            node = node.lchild
        else:
            node = node.rchild
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
                if self.hot.lchild:
                    node.lchild = self.hot.lchild
                    self.hot.lchild = node.lchild
                    self.update_height_above(node.lchild)
                else:
                    self.hot.lchild = node.lchild
                    self.update_height_above(self.hot)
            else:
                if self.hot.rchild:
                    node.rchild = self.hot.rchild
                    self.hot.rchild = node.rchild
                    self.update_height_above(node.rchild)
                else:
                    self.hot.rchild = node.rchild
                    self.update_height_above(self.hot)
            self._size += 1
            # self.update_height_above(self.hot)
        return node


def gen_binary_search_tree():
    bst = BinarySearchTree()
    bst.insert_as_root(36)

    bst.insert(6)
    #
    # node = bst.search(27)
    # print('node:--', node, 'hot:---', bst.hot)

    # print(bst.root, bst.root.lchild)
    # bst.insert(27)

    # for i in [6, 27]:
    #     bst.insert(i)
    return bst


if __name__ == '__main__':
    bst = gen_binary_search_tree()
    # print(bst.root, bst.root.lchild, bst.root.lchild.lchild)
    # print(bst.size)
    for i in bst.trave_in():
        print(i.key)

