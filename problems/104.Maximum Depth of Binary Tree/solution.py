from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(1, root)]
        result = 0
        while stack:
            current_depth, current = stack.pop()
            if current:
                result = max(result, current_depth)
            if current.left:
                stack.append((current_depth + 1, current.left))
            if current.right:
                stack.append((current_depth + 1, current.right))
        return result
