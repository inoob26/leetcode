"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        if not node:
            return node

        queue = [node]
        visited = {}
        visited[node] = Node(node.val, [])

        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]
