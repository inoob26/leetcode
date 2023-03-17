class Solution:

    month_days_map = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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

    def days_since_start(self, day, month, year) -> int:
        days = 0
        # calculate year days
        for y in range(year - 1, 1970, -1):
            days += 365
            if self.is_leap_year(y):
                days += 1
        # calculate month days
        days += sum(self.month_days_map[: month - 1])
        days += day
        if self.is_leap_year(year) and month > 2:
            days += 1
        return days

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday_names = (
            "Friday",
            "Saturday",
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
        )
        today = self.days_since_start(17, 3, 2023)
        input_days = self.days_since_start(day, month, year)
        return weekday_names[(input_days - today) % 7]
