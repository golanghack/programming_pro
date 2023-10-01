#! /usr/bin/env python3 

from BalancedBSTNode import BalancedBSTNode, BalancedBST
from typing import Any

class WBTreeNode(BalancedBSTNode):

    def new_node(self, key: Any, value: Any):
        return WBTreeNode(key, value)

    def too_light(self, other) -> bool:
        other_lenght = len(other) if other else 0 
        return len(self) + 1 >= 4 * (other_lenght + 1)

    def re_balance(self):
        if self.too_light(self.left):
            if self.too_light(self.right.right):
                self.right = self.right.rotate_right()
            new_root = self.rotate_left()
        elif self.too_light(self.right):
            if self.too_light(self.left.left):
                self.left = self.left.rotate_left()
            new_root = self.rotate_right()
        else:
            return self
        return new_root

    def put(self, key: Any, value: Any):
        new_root = BalancedBSTNode.put(self, key, value)
        return new_root.re_balance()

    def remove(self, key: Any):
        new_root = BalancedBSTNode.remove(self, key)
        return new_root.re_balance() if new_root else None

class WBTree(BalancedBST):

    Node = WBTreeNode
    

    