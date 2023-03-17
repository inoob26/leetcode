class Solution:
    month_num_map = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12",
    }

    def _convert_num(self, num: str) -> str:
        n = num[:-2]

        if int(n) < 10:
            return f"0{n}"
        else:
            return n

    def reformatDate(self, date: str) -> str:
        day, month_name, year = date.split()
        month = self.month_num_map[month_name]
        day = self._convert_num(day)
        return f"{year}-{month}-{day}"
