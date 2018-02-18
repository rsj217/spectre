#!/usr/bin/env python
# -*- coding:utf-8 -*-

from spectre.tree.node import BTNode

class BTree(object):

    def __init__(self, order=3):
        self._size = 0
        self._order = order
        self._root = None
        self._hot = None

    def __iter__(self):
        yield from self.inorder(self.root)

    @property
    def size(self):
        return self._size

    @property
    def order(self):
        return self._order

    @property
    def root(self):
        return self._root

    @property
    def empty(self):
        return not self._root

    def search(self, key):
        node = self._root
        self._hot = None

        while node:
            r = self.key_search(node.key, key=key)
            if 0 <= r and key == node.key[r]:
                return node
            self._hot = node
            node = node.child[r + 1]

        return None

    def insert(self, key):
        node = self.search(key)
        if node:
            return False
        r = self.key_search(self._hot._key, key)
        self.key_insert(self._hot._key, r + 1, key)
        self.key_insert(self._hot._child, r + 2, None)
        # self._hot._child.append(None)
        self._size += 1
        self.solve_overflow(self._hot)
        return True

    def remove(self):
        pass

    def solve_overflow(self, node):
        if self._order >= len(node.child):
            return
        s = self._order // 2
        u = BTNode()
        j = 0
        while j < self._order - s - 1:
            self.key_insert(u.child, j, self.key_remove(node.child, s + 1))
            self.key_insert(u.key, j, self.key_remove(node.key, s + 1))
            j += 1

        u.child[self._order - s - 1] = self.key_remove(node.child, s + 1)

        if u.child[0]:
            j = 0
            while j < self._order - s:
                u.child[j]._parent = u
                j += 1

        p = node.parent

        if not p:
            self._root = p = BTNode()
            p.child[0] = node
            node.parent = p

        r = 1 + self.key_search(p.key, node.key[0])
        self.key_insert(p.key, r, self.key_remove(node.key, s))
        self.key_insert(p.child, r + 1, u)
        u._parent = p
        self.solve_overflow(p)

    def solve_underflow(self):
        pass

    def key_search(self, lst, key):
        n = len(lst) - 1
        while 0 <= n:
            if lst[n] <= key:
                break
            n -= 1
        return n

    def key_insert(self, lst, rank, key):
        lst.insert(rank, key)
        return lst

    def key_remove(self, lst, rank):
        return lst.pop(rank)

    def insert_as_root(self, node):
        self._root = node
        self._size += 1

    def inorder(self, node):
        if not node:
            return
        for i in range(len(node.key)):
            yield from self.inorder(node.child[i])
            yield node.key[i]
        yield from self.inorder(node.child[len(node.key)])


if __name__ == '__main__':
    from spectre.tree.node import BTNode

    n53 = BTNode()
    n53.insert_as_root(key=53)

    n36 = BTNode(parent=n53)
    n36._key = [36]

    n7789 = BTNode(parent=n53)
    n7789._key = [77, 89]
    n53._child = [n36, n7789]

    n19 = BTNode(parent=n36)
    n19._key = [19]
    n19._child.append(None)

    n4151 = BTNode(parent=n36)
    n4151._key = [41, 51]
    n4151._child = [None, None, None]

    n36._child = [n19, n4151]

    n75 = BTNode(parent=n7789)
    n75._key = [75]
    n75._child = [None, None]

    n97 = BTNode(parent=n7789)
    n97._key = [97]
    n97._child = [None, None]

    n7984 = BTNode(parent=n7789)
    n7984._key = [79, 84]
    n7984._child = [None, None, None]

    n7789._child = [n75, n7984, n97]

    bt = BTree()
    bt.insert_as_root(n53)
    bt._size = 8

    r = bt.search(19)
    print(r)
