class Solution:
    def findMaxFish(self, grid: list[list[int]]) -> int:
        # this problem is basically just number of islands but finding the max island
        res = 0

        for i, row in enumerate(grid):
            for j, fish in enumerate(row):
                if fish > 0:
                    res = max(res, self.dfs(grid, i, j))
        return res

    def dfs(self, grid: list[list[int]], i: int, j: int) -> int:
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] > 0:
            value = grid[i][j]

            grid[i][j] = 0

            return (
                value
                + self.dfs(grid, i + 1, j)
                + self.dfs(grid, i - 1, j)
                + self.dfs(grid, i, j + 1)
                + self.dfs(grid, i, j - 1)
            )

        return 0
