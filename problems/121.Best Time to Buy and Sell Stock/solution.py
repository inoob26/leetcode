from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


# my bad approach =(
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         data_map = {
#             "min": {"index": None, "val": 100},
#             "max": {"index": None, "val": 1},
#         }

#         for index, price in enumerate(prices):
#             if price > data_map["max"]["val"]:
#                 data_map["max"]["val"] = price
#                 data_map["max"]["index"] = index

#             if price < data_map["max"]["val"] and price < data_map["min"]["val"]:
#                 data_map["min"]["val"] = price
#                 data_map["min"]["index"] = index
#                 if isinstance(data_map["max"]["index"], int) and (
#                     data_map["min"]["index"] > data_map["max"]["index"]
#                 ):
#                     data_map["max"]["index"] = None
#                     data_map["max"]["val"] = 0
#                 continue

#         result = 0
#         if data_map["min"]["index"] and data_map["max"]["index"]:
#             if (data_map["min"]["index"] < data_map["max"]["index"]) and (
#                 data_map["max"]["val"] > data_map["min"]["val"]
#             ):
#                 result = data_map["max"]["val"] - data_map["min"]["val"]

#         return result
