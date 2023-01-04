# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        p_val = p.val
        q_val = q.val

        node = root
        while node:
            current_val = node.val

            if p_val < current_val and q_val < current_val:
                node = node.left
            elif p_val > current_val and q_val > current_val:
                node = node.right
            else:
                return node
