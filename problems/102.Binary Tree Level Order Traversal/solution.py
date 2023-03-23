from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        level = 0
        queue = deque([root])
        while queue:
            result.append([])
            level_len = len(queue)

            for indx in range(level_len):
                node = queue.popleft()
                result[level].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return result
        # v2 MY VERSION
        # queue = [(0, root)]
        # result = [[root.val]]
        # tmp = []
        # prev_level = -1
        # while queue:
        #     level, current = queue.pop(0)
        #     if prev_level != level:
        #         if tmp:
        #             result.append(tmp)
        #             tmp = []
        #         prev_level = level
        #     if current.left:
        #         tmp.append(current.left.val)
        #         queue.append((level+1, current.left))
        #     if current.right:
        #         tmp.append(current.right.val)
        #         queue.append((level+1, current.right))
        # return result

        # v1
        # def helper(node: Optional[TreeNode], level: int):
        #     if len(result) == level:
        #         result.append([])
        #     result[level].append(node.val)

        #     if node.left:
        #         helper(node.left, level + 1)
        #     if node.right:
        #         helper(node.right, level + 1)

        # helper(root, 0)
        # return result
