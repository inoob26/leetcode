class Solution:

    month_days_map = {
        0: 0,
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    def is_leap_year(self, year: int) -> bool:
        if year % 400 == 0:
            result = True
        elif year % 100 == 0:
            result = False
        elif year % 4 == 0:
            result = True
        else:
            result = False

        return result

    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split("-")

        result = 0
        for m in range(int(month)):
            result += self.month_days_map.get(m, 0)

        result += int(day)
        if self.is_leap_year(int(year)) and month > 2:
            return result + 1

        return result
