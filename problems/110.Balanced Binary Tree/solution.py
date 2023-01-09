from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hight(self, root: TreeNode):
        if root == None:
            return 0
        return max(self.hight(root.left), self.hight(root.right)) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        lh = self.hight(root.left)
        rh = self.hight(root.right)

        if (
            abs(lh - rh) < 2
            and self.isBalanced(root.left) is True
            and self.isBalanced(root.right) is True
        ):
            return True

        return False
