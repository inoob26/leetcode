from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, new_color: int
    ) -> List[List[int]]:
        r_size = len(image)
        c_size = len(image[0])
        current_color = image[sr][sc]
        if current_color == new_color:
            return image

        def dfs(row, column):
            if image[row][column] == current_color:
                image[row][column] = new_color
                if row >= 1:
                    dfs(row - 1, column)
                if row + 1 < r_size:
                    dfs(row + 1, column)
                if column >= 1:
                    dfs(row, column - 1)
                if column + 1 < c_size:
                    dfs(row, column + 1)

        dfs(sr, sc)
        return image
