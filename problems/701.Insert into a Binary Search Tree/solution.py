from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        while node:
            if not node.left and not node.right:
                new_leaf = TreeNode(val)
                if node.val < val:
                    node.right = new_leaf
                else:
                    node.left = new_leaf
                return root

            if node.val < val:
                node = node.right
            else:
                node = node.left
        return root
