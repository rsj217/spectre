#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tree.node import BSNode
from tree.binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):

    def __init__(self, root=None):
        super(BinarySearchTree, self).__init__(root=root)
        self.hot = None

    def __repr__(self):
        return self.print_tree()

    def print_tree(self):
        queue = []
        node = self.root
        node._number = 1
        queue.append(node)
        last_index = 1
        tree_str_arr = []

        d = {}
        while queue:
            node = queue.pop(0)
            deep = node.deep
            is_first = bool(d.setdefault(deep, True))
            arr_index = self.cal_arr_index(node, deep)
            if is_first:
                d[deep] = False
                s = '{}{}{}'.format('\n', '  ' * arr_index, str(node.key))
            else:
                s = '{}{}'.format('  ' * (arr_index - last_index - 1), str(node.key))
            tree_str_arr.append(s)

            if node.lchild:
                node.lchild._number = 2 * node._number - 1
                queue.append(node.lchild)

            if node.rchild:
                node.rchild._number = 2 * node._number
                queue.append(node.rchild)

            last_index = arr_index
            del node._number
        del d
        s = ''.join(tree_str_arr)
        return f'<{self.__class__.__name__}>({s}\n)'

    def search(self, e):
        return self._search_in(self.root, e)

    def find(self, e):
        return self._find_in(e)

    def _search_in(self, node, e):
        if node is None or node.key == e:
            return node
        self.hot = node
        if node.key < e:
            node = node.rchild
        else:
            node = node.lchild
        return self._search_in(node, e)

    def _find_in(self, e):
        node = self._root
        while node:
            self.hot = node
            if node.key < e:
                node = node.rchild
            elif e < node.key:
                node = node.lchild
            else:
                self.hot = node.parent
                return node
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

    def remove(self, e):
        node = self.search(e)
        if not node:
            return False
        self._remove_at(node)
        self._size -= 1
        self.update_height_above(self.hot)
        return True

    def _swap(self, na, nb):
        na.key, nb.key = nb.key, na.key
        na.data, nb.data = nb.data, na.data
        return na, nb

    def _remove_at(self, node):
        self.hot = node.parent
        if not node.lchild:
            succ = node.rchild
        elif not node.rchild:
            succ = node.lchild
        else:
            succor = node.succ
            self._swap(node, succor)
            self.hot = succor.parent
            succ = succor.rchild
            node = succor

        if succ:
            succ.parent = self.hot
        else:
            node.parent = succ

        if node is self.hot.lchild:
            self.hot.lchild = succ
        else:
            self.hot.rchild = succ

        del node
        return succ

    @property
    def minimum(self):
        node = self._root
        while True:
            if node.lchild:
                node = node.lchild
            else:
                break
        return node

    @property
    def maximum(self):
        node = self._root
        while True:
            if node.rchild:
                node = node.rchild
            else:
                break
        return node

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


def gen_binary_search_tree():
    """
    <BinarySearchTree>(
                                  36
                  27                              58
          16                              53              69
                                      40              64
                                        46
    )
    """
    bst = BinarySearchTree()
    bst.insert_as_root(36)

    bst.insert(27)
    bst.insert(16)
    bst.insert(58)
    bst.insert(53)
    bst.insert(40)
    bst.insert(46)
    bst.insert(69)
    bst.insert(64)

    return bst


if __name__ == '__main__':
    bst = gen_binary_search_tree()
    print(bst)
    #
    # print(bst.find(53))
    # print('hot', bst.hot)
