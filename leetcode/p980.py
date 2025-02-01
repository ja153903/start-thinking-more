from collections import deque

DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))


class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        result = 0

        start, end = None, None

        num_non_obstacle_cells = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    start = (i, j)

                if grid[i][j] == 2:
                    end = (i, j)

                if grid[i][j] != -1:
                    num_non_obstacle_cells += 1

        assert start
        assert end

        queue = deque()

        queue.append([start, f"({start[0]},{start[1]})", 1])

        unique_paths = set()

        while queue:
            (row, col), path, num_non_obstacle_cells_so_far = queue.popleft()

            if (
                path not in unique_paths
                and num_non_obstacle_cells_so_far == num_non_obstacle_cells
                and (row, col) == end
            ):
                unique_paths.add(path)
                result += 1
                continue

            for dr, dc in DIRS:
                nr, nc = row + dr, col + dc
                if f"({nr},{nc})" in path:
                    continue

                if (
                    0 <= nr < len(grid)
                    and 0 <= nc < len(grid[0])
                    and grid[nr][nc] != -1
                ):
                    queue.append(
                        [
                            (nr, nc),
                            f"{path},({nr},{nc})",
                            num_non_obstacle_cells_so_far + 1,
                        ]
                    )

        return result
