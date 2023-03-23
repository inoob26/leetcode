from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # v2
        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (
                (left.val == right.val)
                and is_mirror(left.left, right.right)
                and is_mirror(left.right, right.left)
            )

        return is_mirror(root.left, root.right)
        # v1
        # queue = [root, root]
        # while queue:
        #     p1 = queue.pop(0)
        #     p2 = queue.pop(0)

        #     if not p1 and not p2:
        #         continue
        #     if not p1 or not p2:
        #         return False
        #     if p1.val != p2.val:
        #         return False

        #     queue.append(p1.left)
        #     queue.append(p2.right)
        #     queue.append(p1.right)
        #     queue.append(p2.left)

        # return True
