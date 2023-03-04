from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # v2
        MEDALS = {
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal",
        }

        def _get_place(place: int) -> str:
            return MEDALS.get(place, str(place))

        ranks = {
            num: indx for indx, num in enumerate(sorted(score, reverse=True), start=1)
        }
        return [_get_place(ranks[num]) for num in score]

        # v1
        # tmp_map = {score: indx for indx, score in enumerate(score)}
        # tmp_ranks = []
        # result = []
        # counter = 1
        # while counter <= len(score):
        #     max_n = max(tmp_map.keys())
        #     if counter == 1:
        #         val = (tmp_map[max_n], "Gold Medal")
        #     elif counter == 2:
        #         val = (tmp_map[max_n], "Silver Medal")
        #     elif counter == 3:
        #         val = (tmp_map[max_n], "Bronze Medal")
        #     else:
        #         val = (tmp_map[max_n], str(counter))

        #     tmp_ranks.append(val)
        #     del tmp_map[max_n]
        #     counter += 1
        # tmp_ranks.sort()
        # return [val[1] for val in tmp_ranks]
