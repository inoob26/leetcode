class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t = {}
        map_t_s = {}
        for s_c, t_c in zip(s, t):
            if s_c not in map_s_t.keys() and t_c not in map_t_s:
                map_s_t[s_c] = t_c
                map_t_s[t_c] = s_c

            elif map_s_t.get(s_c, "") != t_c or map_t_s.get(t_c, "") != s_c:
                return False

        return True
