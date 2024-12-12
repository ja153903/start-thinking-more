import os
from collections import deque, defaultdict


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return [list(line) for line in f.read().strip().split("\n")]


FOUR_DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def part1():
    grid: list[list[str]] = parse_input()
    rows, cols = len(grid), len(grid[0])

    visited: set[tuple[int, int]] = set()

    res = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                queue: deque[tuple[int, int]] = deque()
                char = grid[i][j]
                queue.append((i, j))
                area, perimeter = 0, 0

                while queue:
                    r, c = queue.popleft()
                    if (r, c) in visited:
                        continue

                    visited.add((r, c))

                    area += 1

                    for dr, dc in FOUR_DIRECTIONS:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                            queue.append((nr, nc))
                        else:
                            perimeter += 1

                res += area * perimeter

    return res


def part2():
    grid: list[list[str]] = parse_input()
    rows, cols = len(grid), len(grid[0])

    visited: set[tuple[int, int]] = set()

    res = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                queue: deque[tuple[int, int]] = deque()
                char = grid[i][j]
                queue.append((i, j))
                area, perimeter = 0, 0
                perimeters_by_direction: defaultdict[
                    tuple[int, int], set[tuple[int, int]]
                ] = defaultdict(set)

                while queue:
                    r, c = queue.popleft()
                    if (r, c) in visited:
                        continue

                    visited.add((r, c))

                    area += 1

                    for dr, dc in FOUR_DIRECTIONS:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == char:
                            queue.append((nr, nc))
                        else:
                            perimeter += 1
                            perimeters_by_direction[(dr, dc)].add((nr, nc))

                sides = 0

                for values in perimeters_by_direction.values():
                    seen_values: set[tuple[int, int]] = set()

                    for pr, pc in values:
                        if (pr, pc) not in seen_values:
                            sides += 1
                            queue = deque()
                            queue.append((pr, pc))

                            while queue:
                                r, c = queue.popleft()
                                if (r, c) in seen_values:
                                    continue
                                seen_values.add((r, c))
                                for dr, dc in FOUR_DIRECTIONS:
                                    nr, nc = r + dr, c + dc
                                    # if the next value goes in the same direction, then we keep going
                                    if (nr, nc) in values:
                                        queue.append((nr, nc))

                res += area * sides

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 12")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
