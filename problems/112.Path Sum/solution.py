from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return 0 == targetSum
        sum = targetSum
        # (node, sum - node.val )
        stack = [(root, sum - root.val)]
        while stack:
            current, current_sum = stack.pop()
            if not current.left and not current.right and current_sum == 0:
                return True

            if current.left:
                stack.append((current.left, current_sum - current.left.val))
            if current.right:
                stack.append((current.right, current_sum - current.right.val))

        return False
