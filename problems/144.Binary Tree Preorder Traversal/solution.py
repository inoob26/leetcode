from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # v1
        if root == None:
            return []

        stack = [root]
        result = []
        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result

        # v2
        # if not root:
        #     return []
        # left = self.preorderTraversal(root.left)
        # right = self.preorderTraversal(root.right)

        # return [root.val] + left + right
