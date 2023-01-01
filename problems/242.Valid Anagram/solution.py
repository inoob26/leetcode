class Solution:
    # time complexity O(n)
    # space complexity O(1) because we use hashmap (dict). Using it it doesn't matter wich size is it.
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True

        if len(s) != len(t):
            return False

        origin_map = {}
        for item in s:
            if item in origin_map:
                origin_map[item] += 1
            else:
                origin_map[item] = 0

        for item in t:
            if not item in origin_map.keys():
                return False

            if origin_map[item] > 0:
                origin_map[item] -= 1
            else:
                del origin_map[item]

        return origin_map == {}


# more elegant solution
# time complexity O(n log n)
# space complexity O(1)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
