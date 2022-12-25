from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def add_chield(self, data):
        if data == self.val:
            return

        if data < self.val:
            if self.left:
                self.left.add_chield(data)
            else:
                self.left = TreeNode(data)
        else:
            if self.right:
                self.right.add_chield(data)
            else:
                self.right = TreeNode(data)

    def pre_order_traversal(self):
        elements = [self.val]
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()
        elements += [self.val]
        return elements

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        elements += [self.val]

        if self.right:
            elements += self.right.post_order_traversal()

        return elements


def build_tree(elements):
    root = TreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_chield(elements[i])

    return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
