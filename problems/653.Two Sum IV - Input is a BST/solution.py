from typing import Optional, Set

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # v2 recursion
        hash_pair_val = set()

        def findSum(node: Optional[TreeNode], k: int, hash_pair_val: Set[int]) -> bool:
            if not node:
                return False
            if k - node.val in hash_pair_val:
                return True

            hash_pair_val.add(node.val)
            return findSum(node.left, k, hash_pair_val) or findSum(
                node.right, k, hash_pair_val
            )

        return findSum(root, k, hash_pair_val)
        # v1 BFS
        # if not root:
        #     return False

        # hash_pair_val = set()
        # queue = [root]
        # while queue:
        #     current = queue.pop(0)
        #     if current.val in hash_pair_val:
        #         return True
        #     elif (
        #         current.left
        #         and current.right
        #         and current.left.val + current.right.val == k
        #     ):
        #         return True
        #     hash_pair_val.add(k - current.val)
        #     if current.left:
        #         queue.append(current.left)
        #     if current.right:
        #         queue.append(current.right)
        # return False
