from typing import List
from collections import defaultdict


class Solution:
    def largestPathValue(self, colors, edges):
        size = len(colors)
        vertex = [[] for _ in range(size)]
        couter_color_map = [[0] * 26 for _ in range(size)]
        indegrees = [0] * size

        for edge in edges:
            vertex[edge[0]].append(edge[1])
            indegrees[edge[1]] += 1

        queue = []
        for i in range(size):
            if indegrees[i] == 0:
                queue.append(i)

        res, processed = 0, 0
        while queue:
            q1 = []
            for node in queue:
                processed += 1
                res = max(res, couter_color_map[node][ord(colors[node]) - ord("a")] + 1)
                couter_color_map[node][ord(colors[node]) - ord("a")] += 1
                for neighbor in vertex[node]:
                    for k in range(26):
                        couter_color_map[neighbor][k] = max(
                            couter_color_map[neighbor][k], couter_color_map[node][k]
                        )
                    indegrees[neighbor] -= 1
                    if indegrees[neighbor] == 0:
                        q1.append(neighbor)
            queue = q1

        return res if processed == size else -1


# my solution Not cover all cases
# class Solution:
#     def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
#         verts = defaultdict(list)

#         for indx in range(len(edges)):
#             from_n, to_n = edges[indx]
#             if from_n == to_n:
#                 return -1
#             verts[from_n].append(to_n)

#         colors_counter = {}
#         for color in colors:
#             if color not in colors_counter:
#                 colors_counter[color] = 0

#         queue = [edges[0][0]]
#         seen = set()
#         while queue:
#             curr = queue.pop()
#             if curr in seen:
#                 continue
#             seen.add(curr)
#             colors_counter[colors[curr]] += 1
#             for neighbor in verts[curr]:
#                 queue.append(neighbor)

#         return max(colors_counter.values())
