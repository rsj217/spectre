#!/usr/bin/env python
# -*- coding:utf-8 -*-


class BinNode(object):

    def __init__(self, parent=None, lchild=None, rchild=None, data=None):
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild
        self.data = data
        self.height = 0

    def __repr__(self):
        pdata = getattr(self.parent, 'data', None)
        ldata = getattr(self.lchild, 'data', None)
        rdata = getattr(self.rchild, 'data', None)
        return f'<BinNode>([{pdata}] {ldata}-{self.data}-{rdata}: {self.height})'

    def insert_as_lc(self, e):
        node = BinNode(parent=self, data=e)
        self.lchild = node
        return node

    def insert_as_rc(self, e):
        node = BinNode(parent=self, data=e)
        self.rchild = node
        return node

    @property
    def size(self):
        s = 1
        if self.lchild:
            s += self.lchild.size
        if self.rchild:
            s += self.rchild.size
        return s

    @property
    def succ(self):
        node = self
        if node.rchild:
            node = node.rchild
            while node.lchild:
                node = node.lchild
        else:
            while node.parent and node.parent.rchild == node:
                node = node.parent
            node = node.parent
        return node

    @property
    def precu(self):
        return

    @property
    def deep(self):
        d = -1
        node = self
        while node:
            node = node.parent
            d += 1
        return d

    @property
    def is_root(self):
        return not self.parent

    @property
    def is_lchild(self):
        return self is self.parent.lchild

    @property
    def is_rchild(self):
        return self is self.parent.rchild

    @property
    def has_parent(self):
        return not self.is_root

    @property
    def has_lchild(self):
        return self.lchild

    @property
    def has_rchild(self):
        return self.rchild

    @property
    def has_child(self):
        return self.has_lchild or self.has_rchild

    @property
    def has_both_child(self):
        return self.has_lchild and self.has_rchild

    @property
    def is_leaf(self):
        return not self.has_child

    # Iter
    def trav_preorder(self):
        stack = []
        node = self
        while True:
            while node:
                yield node
                stack.append(node)
                node = node.lchild
            if not stack:
                break
            node = stack.pop()
            node = node.rchild

    def trav_inorder(self):
        stack = []
        node = self
        while True:
            while node:
                stack.append(node)
                node = node.lchild

            if not stack:
                break
            node = stack.pop()
            yield node
            node = node.rchild

    def trav_postorder(self):
        stack = []
        node = self
        last_visit = None
        while True:
            while node:
                stack.append(node)
                node = node.lchild

            if not stack:
                break

            if stack[-1].rchild is not last_visit:
                node = stack[-1].rchild
                last_visit = None
            else:
                last_visit = stack.pop()
                yield last_visit

    def trav_levelorder(self):
        queue = []
        node = self
        queue.append(node)
        while queue:
            node = queue.pop(0)
            yield node
            if node.lchild:
                queue.append(node.lchild)
            if node.rchild:
                queue.append(node.rchild)

    # Recursive
    def preorder(self):
        node = self
        yield from self._preorder(node)

    def inorder(self):
        node = self
        yield from self._inorder(node)

    def postorder(self):
        node = self
        yield from self._postorder(node)

    def _preorder(self, node):
        if not node:
            return
        yield node
        yield from self._preorder(node.lchild)
        yield from self._preorder(node.rchild)

    def _inorder(self, node):
        if not node:
            return
        yield from self._inorder(node.lchild)
        yield node
        yield from self._inorder(node.rchild)

    def _postorder(self, node):
        if not node:
            return
        yield from self._postorder(node.lchild)
        yield from self._postorder(node.rchild)
        yield node

    def trave_pre(self):
        stack = []
        node = self
        while True:
            if node:
                yield node
                stack.append(node)
                node = node.lchild
            elif not stack:
                break
            else:
                node = stack.pop()
                node = node.rchild

    def trave_pre1(self):
        stack = []
        node = self
        while stack or node:
            if node:
                yield node
                stack.append(node)
                node = node.lchild
            else:
                node = stack.pop()
                node = node.rchild

    def trave_pre2(self):
        stack = []
        node = self
        while True:
            while node:
                yield node
                if node.has_rchild:
                    stack.append(node.rchild)
                node = node.lchild
            if not stack:
                break
            node = stack.pop()

    def trave_pre3(self):
        stack = []
        node = self
        stack.append(node)
        while stack:
            node = stack.pop()
            yield node
            if node.has_rchild:
                stack.append(node.rchild)
            if node.has_lchild:
                stack.append(node.lchild)

    def inorder_py2(self):
        node = self
        for x in self._inorder_py2(node):
            yield x

    def _inorder_py2(self, node):
        if not node:
            return
        for x in self._inorder_py2(node.lchild):
            yield x
        yield node
        for x in self._inorder_py2(node.rchild):
            yield x


class Entry(object):

    def __init__(self, key, value=None):
        self._key = key
        self._value = value or key

    def __gt__(self, other):
        return self._key > other._key

    def __ge__(self, other):
        return self._key >= other._key

    def __lt__(self, other):
        return self._key < other._key

    def __le__(self, other):
        return self._key <= other._key

    def __eq__(self, other):
        return self._key == other._key

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value


class BSNode(BinNode):

    def __init__(self, key, value, parent=None):
        super(BSNode, self).__init__(parent=parent, lchild=None, rchild=None, data=None)
        self._entry = Entry(key=key, value=value)

    def __repr__(self):
        pdata = getattr(self.parent, 'key', None)
        ldata = getattr(self.lchild, 'key', None)
        rdata = getattr(self.rchild, 'key', None)
        return f'<BSNode>([{pdata}] {ldata}-{self.key}-{rdata}: {self.height} - {self.value})'

    @property
    def key(self):
        return self._entry.key

    @key.setter
    def key(self, value):
        self._entry._key = value

    @property
    def value(self):
        return self._entry.value

    @value.setter
    def value(self, value):
        self._entry._value = value

    @property
    def floor(self):
        return

    @property
    def ceil(self):
        return

    @property
    def rank(self):
        return

    @property
    def select(self):
        return

    def insert_as_lc(self, e):
        raise NotImplementedError

    def insert_as_rc(self, e):
        raise NotImplementedError


class BTNode(object):

    def __init__(self, parent=None, key=None):
        self._parent = parent
        if key:
            _key, _child = [key], [None, None]
        else:
            _key, _child = [], [None]

        self._key = _key
        self._child = _child

    def __repr__(self):
        parent = self._parent._key if self._parent else None
        child = [getattr(child, 'key', None) for child in self._child]
        return '<BTNode>(parent:{} key:{} child:{})'.format(parent, self._key, child)

    @property
    def parent(self):
        return self._parent

    @property
    def key(self):
        return self._key

    @property
    def child(self):
        return self._child

    @property
    def is_leaf(self):
        for i in self._child:
            if i is not None:
                return False
        return True


if __name__ == '__main__':
    pass
