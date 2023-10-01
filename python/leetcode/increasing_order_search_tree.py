#! /usr/bin/env python3 
""" 
TASK -> 

DESC
Constraints:
Given a binary search tree, rearrange the tree in in-order so that the leftmost
node in the tree is now the root of the tree, and every node has no left child a
nd only 1 right child.
 NOTE
 The number of nodes in the given tree will be between 1 and 100.
 Each node will have a unique integer value from 0 to 1000.

EXAMPLE
Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 Time: O(n)
 Space: O(h)
""" 

import typing

class TreeNode(object):
    """Tree node from object""" 

    def __init__(self, x: int) -> None:
        self.val = x 
        self.left = None 
        self.right = None

class Solution(object):
    """Solution class from object""" 

    def increasingBST(self, root: int) -> typing.Callable:
        """root -> TreeNode 
           rtype -> TreeNode
        """ 

        def increasingBST_helper(root: int, tail: int) -> typing.Callable:
            if not root:
                return tail
            result = increasingBST_helper(root.left, root)
            root.left = None 
            root.right = increasingBST_helper(root.right, tail)
            return result
        return increasingBST_helper(root, None)