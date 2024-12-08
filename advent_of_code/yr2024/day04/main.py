import os

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        raw = f.read().strip().split("\n")
        result: list[list[int]] = []

        for line in raw:
            row: list[int] = []
            for ch in line.strip():
                match ch:
                    case "X":
                        row.append(1)
                    case "M":
                        row.append(2)
                    case "A":
                        row.append(3)
                    case "S":
                        row.append(4)
                    case _:
                        continue
            result.append(row)

        return result


DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))


def part1():
    grid = parse_input()
    res = 0

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col == 1:
                for di, dj in DIRECTIONS:
                    ci, cj = i, j
                    cur_itr = 1

                    while (
                        0 <= ci <= len(grid) and 0 <= cj <= len(grid[0]) and cur_itr < 4
                    ):
                        ni, nj = ci + di, cj + dj
                        if (
                            ni < 0
                            or nj < 0
                            or ni >= len(grid)
                            or nj >= len(grid[0])
                            or grid[ni][nj] != cur_itr + 1
                        ):
                            break

                        ci, cj = ni, nj
                        cur_itr = grid[ni][nj]

                    if cur_itr == 4:
                        res += 1

    return res


def is_mono_increasing_by_one(lst: list[int]) -> bool:
    for i in range(1, len(lst)):
        if lst[i] - lst[i - 1] != 1:
            return False
    return True


def is_mono_decreasing_by_one(lst: list[int]) -> bool:
    for i in range(1, len(lst)):
        if lst[i - 1] - lst[i] != 1:
            return False
    return True


def is_mas_dos(grid: list[list[int]], row_start: int, col_start: int) -> bool:
    diag_down = [grid[row_start + i][col_start + i] for i in range(3)]
    if not is_mono_increasing_by_one(diag_down) and not is_mono_decreasing_by_one(
        diag_down
    ):
        return False

    diag_up = [grid[row_start + 2 - i][col_start + i] for i in range(3)]
    if not is_mono_increasing_by_one(diag_up) and not is_mono_decreasing_by_one(
        diag_up
    ):
        return False

    return True


def part2():
    grid = parse_input()
    res = 0

    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            if grid[i][j] == 2 or grid[i][j] == 4:
                if is_mas_dos(grid, i, j):
                    res += 1

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 4")

    print(f"Part 1 -> {part1()}")
    print(f"Part 2 -> {part2()}")
