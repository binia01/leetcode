from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if not (0 <= row < row_count and 0 <= col < col_count) or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0  # mark as visited
            area = 1

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                area += dfs(row + dr, col + dc)

            return area

        row_count, col_count = len(grid), len(grid[0])
        max_area = 0

        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))

        return max_area
