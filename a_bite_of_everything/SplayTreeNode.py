#! /usr/bin/env python3

from typing import Any
from BalancedBSTNode import BalancedBSTNode, BalancedBST

class SplayTreeNode(BalancedBSTNode):

    def new_node(self, key: Any, value: Any):
        return SplayTreeNode(key, value)

    def splay_up(self, key: Any):
        new_root = self

        if key < self.key:
            if key < self.left.key:
                new_root = self.rotate_right().rotate_right()
            elif key > self.left.key:
                self.left = self.left.rotate_left()
                new_root = self.rotate_right()
        elif key > self.key:
            if key > self.right.key:
                new_root = self.rotate_left().rotate_left()
            elif key < self.right.key:
                self.right = self.right.rotate_right()
                new_root = self.rotate_left()
        return new_root

    def put(self, key: Any, value: Any):
        new_root = BalancedBSTNode.put(self, key, value)
        return new_root.splay_up(key)

    def get(self, key: Any):
        if key == self.key:
            return self
        elif key < self.key and self.left:
            self.left = self.left.get(key)
        elif key > self.key and self.right:
            self.right = self.right.get(key)
        else:
            raise KeyError
        return self.splay_up(key)

class SplayTree(BalancedBST):

    Node = SplayTreeNode

    def splay_up(self, key:Any):
        if key < self._root.key:
            self._root = self._root.rotate_right()
        if key > self._root.key:
            self._root = self._root.rotate_left()

    def get(self, key: Any):
        if self._root is None: 
            raise KeyError
        self._root = self._root.get(key)
        self.splay_up(key)
        return self._root.value

    def put(self, key: Any, value: Any):
        BalancedBST.put(self, key, value)
        self.splay_up(key)

    
    
