from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # v2
        return not (
            rec2[0] >= rec1[2]  # right
            or rec2[2] <= rec1[0]  # left
            or rec2[1] >= rec1[3]  # up
            or rec2[3] <= rec1[1]  # down
        )

        # v1
        # x1 = set(x for x in range(x1_1, x2_1 + 1 if x2_1 > 0 else x2_1 - 1, 1))
        # y1 = set(y for y in range(y1_1, y2_1 + 1 if y2_1 > 0 else y2_1 - 1, 1))
        # x2 = set(x for x in range(x1_2, x2_2 + 1 if y2_1 > 0 else y2_1 - 1, 1))
        # y2 = set(y for y in range(y1_2, y2_2 + 1 if y2_1 > 0 else x2_2 - 1, 1))

        # x = x1 & x2
        # y = y1 & y2

        # if len(x) > 1 and len(y) > 1:
        #     return True

        # return False
