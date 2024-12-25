import os
import heapq
from typing import NamedTuple
from collections import Counter

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.test.in"


class RegularNode(NamedTuple):
    dist: int
    x: int
    y: int


class CheatNode(NamedTuple):
    dist: int
    x: int
    y: int
    attempts_remaining: int


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return [list(line) for line in f.read().strip().split("\n")]


def find_start_and_end_points(
    grid: list[list[str]],
) -> tuple[tuple[int, int], tuple[int, int]]:
    start, end = None, None

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "S":
                start = (x, y)

            if grid[y][x] == "E":
                end = (x, y)

    if start is None or end is None:
        raise ValueError("Start and/or end points not found in the maze.")

    return start, end


DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))


def dijkstras(maze: list[list[str]]):
    start, end = find_start_and_end_points(maze)

    q: list[RegularNode] = []
    heapq.heappush(q, RegularNode(0, start[0], start[1]))

    visited = set()

    while q:
        dist, x, y = heapq.heappop(q)

        if (x, y) == end:
            return dist

        visited.add((x, y))

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if (
                nx < 0
                or ny < 0
                or nx >= len(maze[0])
                or ny >= len(maze)
                or (nx, ny) in visited
                or maze[ny][nx] == "#"
            ):
                continue

            heapq.heappush(q, RegularNode(dist + 1, nx, ny))


def part1():
    maze = parse_input()

    picosecond_without_cheats = dijkstras(maze)

    counter = Counter()

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "#":
                maze[y][x] = "."
                with_cheats = dijkstras(maze)
                if with_cheats is not None:
                    counter[with_cheats] += 1
                maze[y][x] = "#"

    res = 0
    for key, value in counter.items():
        if picosecond_without_cheats - key >= 100:
            res += value
    return res


def part2():
    # this is going to be similar to part 1, but instead of changing just one
    # we have to construct a path
    maze = parse_input()
    picosecond_without_cheats = dijkstras(maze)

    start, end = find_start_and_end_points(maze)

    counter = Counter()
    visited = set()

    q: list[CheatNode] = []
    heapq.heappush(q, CheatNode(0, start[0], start[1], 20))

    while q:
        dist, x, y, attempts_remaining = heapq.heappop(q)

        if (x, y) == end:
            counter[dist] += 1
            continue

        if (x, y, attempts_remaining) in visited:
            continue

        visited.add((x, y, attempts_remaining))

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (
                nx < 0
                or ny < 0
                or nx >= len(maze[0])
                or ny >= len(maze)
                or (nx, ny, attempts_remaining) in visited
            ):
                continue

            is_wall = maze[ny][nx] == "#"

            if attempts_remaining > 0 and is_wall:
                heapq.heappush(
                    q,
                    CheatNode(dist + 1, nx, ny, attempts_remaining - 1),
                )

            if not is_wall:
                heapq.heappush(
                    q,
                    CheatNode(dist + 1, nx, ny, attempts_remaining),
                )

    res = 0

    for key, value in counter.items():
        if key != picosecond_without_cheats:
            print(
                f"There are {value} cheats that save {picosecond_without_cheats - key} picoseconds"
            )
        # if key != picosecond_without_cheats and picosecond_without_cheats - key >= 100:
        #     res += value

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 20")
    # print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
