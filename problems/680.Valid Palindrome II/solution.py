from collections import Counter


class Solution:
    def check_palindrome(self, s: str, l: int, r: int):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return self.check_palindrome(s, l, r - 1) or self.check_palindrome(
                    s, l + 1, r
                )

            l += 1
            r -= 1
        return True

        # v3
        # chars = list(s)
        # char_map = Counter(s)
        # item_for_delete = None

        # for char, val in char_map.items():
        #     if val % 2 == 0:
        #         continue

        #     item_for_delete = char
        #     break

        # if item_for_delete:
        #     l = 0
        #     r = len(chars) - 1
        #     tmp_arr = [""] * len(chars)
        #     while l < r:
        #         char_l = chars[l]
        #         char_r = chars[r]
        #         if char_l == char_r:
        #             tmp_arr[l] = char_l
        #             tmp_arr[r] = char_r
        #         l += 1
        #         r -= 1
        #     if not all(["" == val for val in tmp_arr]):
        #         chars = tmp_arr
        # tmp_rev = "".join(chars[::-1])
        # chars_str = "".join(chars)
        # return tmp_rev == chars_str

        # v2
        # chars = list(s)
        # char_map = Counter(s)
        # item_for_delete = None
        # # "cbbcc"
        # for char, val in char_map.items():
        #     if val % 2 == 0:
        #         continue

        #     item_for_delete = char
        #     break

        # if item_for_delete:
        #     last_indx = -1
        #     # finding last index for item_for_delete
        #     for indx, item in enumerate(chars):
        #         if item != item_for_delete:
        #             continue

        #         last_indx = indx
        #     chars.pop(last_indx)
        # tmp_rev = "".join(chars[::-1])
        # chars_str = "".join(chars)

        # return tmp_rev == chars_str

        # v1
        # tmp = list(s)
        # tmp_rev = "".join(tmp[::-1])

        # if tmp_rev == s:
        #     return True

        # tmp.pop(len(tmp) // 2)
        # tmp_rev = "".join(tmp[::-1])
        # tmp_str = "".join(tmp)
        # return tmp_rev == tmp_str
