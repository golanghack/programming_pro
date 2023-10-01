#! /usr/bin/env python3 

from BSTMapping import BSTMapping
from BSTNode import BSTNode
from typing import Any

class BalancedBSTNode(BSTNode):
    
    def new_node(self, key: Any, value: Any) -> BalancedBSTNode:
        return BalancedBSTNode(key, value)
    
    def put(self, key: Any, value: Any):
        if key == self.key:
            self.value = value
        elif key < self.key:
            if self.left:
                self.left = self.left.put(key, value)
            else:
                self.left = self.new_node(key, value)
        elif key > self.key:
            if self.right:
                self.right = self.right.put(key, value)
            else:
                self.right = self.new_node(key, value)
        self._update_lenght()
        return self
    
    def rotate_right(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self
        self._update_lenght()
        new_root._update_lenght()
        return new_root
    
    def rotate_left(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self
        self._update_lenght()
        new_root._update_lenght()
        new_root._update_lenght()
        return new_root
    
class BalancedBST(BSTMapping):
    
    Node = BalancedBSTNode
    
    def put(self, key: Any, value: Any):
        if self._root:
            self._root = self._root.put(key, value)
        else:
            self._root = self.Node(key, value)