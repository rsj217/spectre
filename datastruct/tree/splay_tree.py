#!/usr/bin/env python
# -*- coding:utf-8 -*-


from datastruct.tree.binary_search_tree import BinarySearchTree


class SplayTree(BinarySearchTree):

    def attach_as_lc(self, node, lchild):
        node.lchild = lchild
        if lchild:
            lchild.parent = node

    def attach_as_rc(self, node, rchild):
        node.rchild = rchild
        if rchild:
            rchild.parent = node

    def _splay(self, v):
        if v is None:
            return

        p = v.parent
        g = p.parent

        while p and g:
            # g的祖父，如果有祖父，就接入上升的v，如果没有则忽略
            gg = g.parent
            if v.is_lchild:
                if p.is_lchild:
                    # zig-zig
                    self.attach_as_lc(g, v.rchild)
                    self.attach_as_lc(p, p.rchild)
                    self.attach_as_rc(p, g)
                    self.attach_as_rc(v, p)
                else:
                    # zig-zag
                    self.attach_as_rc(g, v.lchild)
                    self.attach_as_lc(p, v.rchild)
                    self.attach_as_lc(v, g)
                    self.attach_as_rc(v, p)

            elif p.is_rchild:
                # zag-zag
                self.attach_as_rc(g, p.lchild)
                self.attach_as_rc(p, v.lchild)
                self.attach_as_lc(p, g)
                self.attach_as_lc(v, p)
            else:
                # zag-zig
                self.attach_as_rc(p, v.lchild)
                self.attach_as_lc(g, v.rchild)
                self.attach_as_rc(v, g)
                self.attach_as_lc(v, p)

            if not gg:
                v.parent = None
            else:
                # 接入上升的v
                if g == gg.lchild:
                    self.attach_as_lc(gg, v)
                else:
                    self.attach_as_rc(gg, v)

            self.update_height(g)
            self.update_height(p)
            self.update_height(v)

            # 第一轮调整之后，v已经上升，接下来再进行调整，直到v到达树根
            p = v.parent
            if not p:
                break
            g = p.parent

        # 针对只有父亲p而没有祖父g的情况，即只需要上升一层
        if p:
            if v.is_lchild:
                # zig
                self.attach_as_lc(p, v.rchild)
                self.attach_as_rc(v, p)
            else:
                # zag
                self.attach_as_rc(p, v.lchild)
                self.attach_as_lc(v, p)

            self.update_height(p)
            self.update_height(v)

        # v已经到达树根，重置其parent为None
        v.parent = None
        return v

    def search(self, e):
        n = self._search_in(self._root, e)
        self._root = self._splay(n)
        return self._root

    def insert(self, e):
        pass

    def remove(self, e):
        pass


if __name__ == '__main__':
    pass
