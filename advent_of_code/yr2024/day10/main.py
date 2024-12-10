import os
from collections import deque

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return [[int(x) for x in list(line)] for line in f.read().strip().split("\n")]


def get_score(m: list[list[int]], r: int, c: int) -> int:
    visited_nine: set[tuple[int, int]] = set()
    queue: deque[tuple[int, int, int]] = deque()
    queue.append((r, c, 0))

    res = 0

    while queue:
        row, col, level = queue.popleft()

        if level == 9:
            if (row, col) not in visited_nine:
                res += 1
                visited_nine.add((row, col))
            continue

        if row + 1 < len(m) and m[row + 1][col] == level + 1:
            queue.append((row + 1, col, level + 1))

        if row - 1 >= 0 and m[row - 1][col] == level + 1:
            queue.append((row - 1, col, level + 1))

        if col + 1 < len(m[0]) and m[row][col + 1] == level + 1:
            queue.append((row, col + 1, level + 1))

        if col - 1 >= 0 and m[row][col - 1] == level + 1:
            queue.append((row, col - 1, level + 1))

    return res


def get_distinct_score(m: list[list[int]], r: int, c: int) -> int:
    queue: deque[tuple[int, int, int]] = deque()
    queue.append((r, c, 0))

    res = 0

    while queue:
        row, col, level = queue.popleft()

        if level == 9:
            res += 1
            continue

        if row + 1 < len(m) and m[row + 1][col] == level + 1:
            queue.append((row + 1, col, level + 1))

        if row - 1 >= 0 and m[row - 1][col] == level + 1:
            queue.append((row - 1, col, level + 1))

        if col + 1 < len(m[0]) and m[row][col + 1] == level + 1:
            queue.append((row, col + 1, level + 1))

        if col - 1 >= 0 and m[row][col - 1] == level + 1:
            queue.append((row, col - 1, level + 1))
    return res


def part1():
    m = parse_input()
    rows, cols = len(m), len(m[0])

    trailheads: deque[tuple[int, int]] = deque()

    for i in range(rows):
        for j in range(cols):
            if m[i][j] == 0:
                trailheads.append((i, j))

    scores = 0

    while trailheads:
        r, c = trailheads.popleft()
        current_score = get_score(m, r, c)

        scores += current_score

    return scores


def part2():
    m = parse_input()
    rows, cols = len(m), len(m[0])

    trailheads: deque[tuple[int, int]] = deque()

    for i in range(rows):
        for j in range(cols):
            if m[i][j] == 0:
                trailheads.append((i, j))

    scores = 0

    while trailheads:
        r, c = trailheads.popleft()
        current_score = get_distinct_score(m, r, c)

        scores += current_score

    return scores


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 10")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
