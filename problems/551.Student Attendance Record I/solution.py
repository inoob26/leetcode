import re


class Solution:
    def checkRecord(self, s: str) -> bool:
        pattern = ".*(A.*A|LLL).*"
        return not re.match(pattern, s)

        # first solution
        # late_counter = 0
        # absent_counter = 0
        # prev_day = ""
        # for record in s:
        #     if record == "A":
        #         absent_counter += 1
        #     elif record == "L":
        #         if late_counter < 3 and prev_day != "L":
        #             late_counter = 0
        #         late_counter += 1
        #     prev_day = record

        # return not (absent_counter >= 2 or late_counter > 2)
