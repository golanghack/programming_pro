#! /usr/bin/env python3 

from BalancedBSTNode import BalancedBSTNode, BalancedBST
from typing import Any 

def height(node):
    return node.height if node else -1 

def update(node):
    if node:
        node._update_lenght()
        node._update_lenght()

class AVLTreeNode(BalancedBSTNode):

    def __init__(self, key: Any, value: Any):
        BalancedBSTNode.__init__(self, key, value)
        self._update_lenght()

    def new_node(self, key: Any, value: Any):
        return AVLTreeNode(key, value)

    def _update_lenght(self):
        self.height = 1 + max(height(self.left), height(self.right))

    def balance(self):
        return height(self.right) - height(self.left)

    def re_balance(self):
        balance = self.balance()
        if balance == -2:
            if self.left.balance() > 0:
                self.left = self.left.rotate_left()
            new_root = self.rotate_right()
        elif balance == 2:
            if self.right.balance() < 0:
                self.right = self.right.rotate_left()
            new_root = self.rotate_left()
        else:
            return self
        update(new_root.left)
        update(new_root.right)
        update(new_root)
        return new_root

    def put(self, key: Any, value: Any):
        new_root = BalancedBSTNode.put(self, key, value)
        update(new_root)
        return new_root.re_balance()

    def remove(self, key: Any):
        new_root = BalancedBSTNode.remove(self, key)
        update(new_root)
        return new_root.re_balance() if new_root else None

class AVLTree(BalancedBST):
    Node = AVLTreeNode