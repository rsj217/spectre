#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tree.node import BinNode


class BinaryTree(object):

    def __init__(self, root=None):
        self._root = root
        self._size = 0

    def __iter__(self):
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

    def cal_arr_index(self, node, deep):
        vheight = self.root.height - deep
        start = 2 ** vheight - 1
        step = 2 ** (vheight + 1)
        arr_index = start + (node._number - 1) * step
        return arr_index

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
                s = '{}{}{}'.format('\n\n', ' ' * arr_index, str(node.data))
            else:
                s = '{}{}'.format(' ' * (arr_index - last_index - 1), str(node.data))
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

    def __repr__(self):
        return self.print_tree()

    @property
    def size(self):
        return self._size

    @property
    def is_empty(self):
        return self.root is None

    @property
    def root(self):
        return self._root

    def attach(self):
        pass

    @staticmethod
    def stature(p):
        if p:
            return p.height
        return -1

    @staticmethod
    def update_height(node):
        lheight = BinaryTree.stature(node.lchild)
        rheight = BinaryTree.stature(node.rchild)
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

    def remove(self, e):
        pass

    def remove_at(self, e):
        pass

    def secede(self, e):
        pass

    # def size(self, e):
    #     pass

    @staticmethod
    def trav_preorder(node):
        yield from node.trav_preorder()

    @staticmethod
    def trav_inorder(node):
        yield from node.trav_inorder()

    @staticmethod
    def trav_postorder(node):
        yield from node.trav_postorder()

    @staticmethod
    def trav_levelorder(node):
        yield from node.trav_levelorder()

    @staticmethod
    def preorder(node):
        yield from node.preorder()

    @staticmethod
    def inorder(node):
        yield from node.inorder()

    @staticmethod
    def postorder(node):
        yield from node.postorder()

    # def trave_pre1(self):
    #     stack = []
    #     node = self.root
    #     while stack or node:
    #         if node:
    #             yield node
    #             stack.append(node)
    #             node = node.lchild
    #         else:
    #             node = stack.pop()
    #             node = node.rchild
    #
    # def trave_pre2(self):
    #     stack = []
    #     node = self.root
    #     need = True
    #     while True:
    #         if need:
    #             while node:
    #                 yield node
    #                 stack.append(node)
    #                 node = node.lchild
    #
    #         if not stack:
    #             break
    #         node = stack.pop()
    #         if node.rchild:
    #             need = True
    #             node = node.rchild
    #         else:
    #             need = False
    #
    # def trave_pre3(self):
    #     stack = []
    #     node = self.root
    #     while True:
    #         while node:
    #             yield node
    #             stack.append(node)
    #             node = node.lchild
    #
    #         if not stack:
    #             break
    #         node = stack.pop()
    #         node = node.rchild
    #
    # def trave_pre4(self):
    #     stack = []
    #     node = self.root
    #     while True:
    #         while node:
    #             yield node
    #             if node.rchild:
    #                 stack.append(node.rchild)
    #             node = node.lchild
    #         if not stack:
    #             break
    #         node = stack.pop()
    #
    # def visit_along_left_branch(self, stack, node):
    #     while node:
    #         yield node
    #         if node.rchild:
    #             stack.append(node.rchild)
    #         node = node.lchild
    #
    # def trave_pre_along_left_branch(self):
    #     stack = []
    #     node = self.root
    #     while True:
    #         yield from self.visit_along_left_branch(stack, node)
    #
    #         if not stack:
    #             break
    #         node = stack.pop()
    #
    # def trave_in(self):
    #     stack = []
    #     node = self.root
    #     while True:
    #         while node:
    #             stack.append(node)
    #             node = node.lchild
    #
    #         if not stack:
    #             break
    #         node = stack.pop()
    #         yield node
    #         node = node.rchild
    #
    # def trave_in2(self):
    #     stack = []
    #     node = self.root
    #     while stack or node:
    #         if node:
    #             stack.append(node)
    #             node = node.lchild
    #         else:
    #             node = stack.pop()
    #             yield node
    #             node = node.rchild
    #
    # def trave_in3(self):
    #     stack = []
    #     node = self.root
    #     while True:
    #         if node:
    #             stack.append(node)
    #             node = node.lchild
    #         elif not stack:
    #             break
    #         else:
    #             node = stack.pop()
    #             yield node
    #             node = node.rchild
    #
    # def trave_post(self):
    #     stack = []
    #     node = self.root
    #     rchild = None
    #     while True:
    #         while node:
    #             stack.append(node)
    #             node = node.lchild
    #         if not stack:
    #             break
    #         if stack[-1].rchild != rchild:
    #             node = stack[-1].rchild
    #             rchild = None
    #         else:
    #             rchild = stack.pop()
    #             yield rchild
    #
    # def trave_post2(self):
    #     stack = []
    #     node = self.root
    #     rchild = None
    #     while stack or node:
    #         if node:
    #             stack.append(node)
    #             node = node.lchild
    #         elif stack[-1].rchild is not rchild:
    #             node = stack[-1].rchild
    #             rchild = None
    #         else:
    #             rchild = stack.pop()
    #             yield rchild
    #
    # def trave_post3(self):
    #     stack = []
    #     node = self.root
    #     last_visit = None
    #     while True:
    #         if node:
    #             stack.append(node)
    #             node = node.lchild
    #         elif not stack:
    #             break
    #         elif stack[-1].rchild != last_visit:
    #             node = stack[-1].rchild
    #             last_visit = None
    #         else:
    #             last_visit = stack.pop()
    #             yield last_visit


if __name__ == '__main__':
    pass
