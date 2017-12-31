#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tree.node import BSNode
from tree.binary_search_tree import BinarySearchTree


class SplayTree(BinarySearchTree):

    def _splay(self, v):
        if v is None:
            return

        p = v.parent
        g = p.parent

        while p and g:

            pass

            p = v.parent
            g = v.parent

        if p:
            if v.is_lchild:
                pass
            else:
                pass
            self.update_height(p)
            self.update_height(v)

        v.parent = None
        return v




    def search(self, e):
        pass

    def insert(self, e):
        pass

    def remove(self, e):
        pass


def gen_splay_tree():
    """
    <AVLTree>(
          58
      53      69
    40  54
    )
    """
    st = SplayTree()
    st.insert_as_root(17)

    st.insert(16)
    st.insert(15)
    st.insert(14)
    st.insert(13)
    st.insert(12)
    st.insert(11)

    print(st)

    return st


if __name__ == '__main__':
    st = gen_splay_tree()
