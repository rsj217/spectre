#!/usr/bin/env python
# -*- coding:utf-8 -*-


class BTree(object):

    def __init__(self, order=3):
        self._size = 0
        self._order = order
        self._root = None
        self._hot = None

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
        # self.key_insert(self._hot._child, r + 2, None)
        self._hot._child.append(None)
        self._size += 1
        self.solve_overflow(self._hot)
        return True

    def remove(self):
        pass

    def solve_overflow(self, node):
        if self._order >= len(node.child):
            return
        r = self._order // 2
        u = BTNode()


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

    def insert_as_root(self, node):
        self._root = node
        self._size += 1


if __name__ == '__main__':
    from spectre.tree.node import BTNode

    root = BTNode()
    root._key.append(25)
    bt = BTree()
    bt.insert_as_root(root)

    n13 = BTNode(parent=root)
    n13._key.append(13)

    n344349 = BTNode(parent=root)
    n344349._key.extend([34, 43, 49])

    root._child.extend([n13, n344349])

    n7 = BTNode(parent=n13)
    n7._key.append(7)
    n7._child.extend([None, None])

    n1922 = BTNode(parent=n13)
    n1922._key.extend([19, 22])
    n1922._child.extend([None, None, None])
    n13._child.extend([n7, n1922])

    n28 = BTNode(parent=n344349)
    n28._key.append(28)
    n28._child.extend([None, None])

    n374041 = BTNode(parent=n344349)
    n374041._key.extend([37, 40, 41])
    n374041._child.extend([None, None, None])

    n46 = BTNode(parent=n344349)
    n46._key.append(46)
    n46._child.extend([None, None])

    n52 = BTNode(parent=n344349)
    n52._key.append(52)
    n52._child.extend([None, None])

    n344349._child.extend([n28, n374041, n46, n52])

    r = bt.search(52)
    print(r)
