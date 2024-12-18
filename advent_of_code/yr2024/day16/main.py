import os
import heapq
import math
from collections import defaultdict
from typing import NamedTuple


class QueueNode(NamedTuple):
    dist: int
    dir: str
    x: int
    y: int


class QueueNodeWithPath(NamedTuple):
    dist: int
    dir: str
    x: int
    y: int
    path: set[str]


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        data = f.read().strip()
        return [list(line.strip()) for line in data.split("\n")]


def find_starting_and_end_point(
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
        raise ValueError("Could not find the appropriate points")

    return start, end


DIRECTIONS = ((1, 0, "E"), (-1, 0, "W"), (0, 1, "S"), (0, -1, "N"))


def part1():
    maze = parse_input()
    start, end = find_starting_and_end_point(maze)

    q: list[QueueNode] = []
    visited = defaultdict(int)

    q.append(QueueNode(0, "E", start[0], start[1]))

    while q:
        u = heapq.heappop(q)

        key = f"({u.x},{u.y}),{u.dir}"

        if u.x == end[0] and u.y == end[1]:
            return u.dist

        visited[key] = u.dist

        for dx, dy, dd in DIRECTIONS:
            nx, ny = u.x + dx, u.y + dy

            next_key = f"({nx},{ny}),{dd}"

            if (
                nx < 0
                or ny < 0
                or nx >= len(maze[0])
                or ny >= len(maze)
                or next_key in visited
                or maze[ny][nx] == "#"
            ):
                continue

            if u.dir != dd:
                heapq.heappush(q, QueueNode(u.dist + 1001, dd, nx, ny))
            else:
                heapq.heappush(q, QueueNode(u.dist + 1, dd, nx, ny))


def part2():
    maze = parse_input()
    start, end = find_starting_and_end_point(maze)

    q: list[QueueNodeWithPath] = []
    visited = defaultdict(int)
    paths_by_score: defaultdict[int, set[str]] = defaultdict(set)

    q.append(QueueNodeWithPath(0, "E", start[0], start[1], set()))
    lowest = math.inf

    while q:
        u = heapq.heappop(q)

        key = f"({u.x},{u.y}),{u.dir}"

        if u.x == end[0] and u.y == end[1]:
            lowest = u.dist
            paths_by_score[u.dist] = paths_by_score[u.dist].union(u.path)

        visited[key] = u.dist

        for dx, dy, dd in DIRECTIONS:
            nx, ny = u.x + dx, u.y + dy

            next_key = f"({nx},{ny}),{dd}"

            if (
                nx < 0
                or ny < 0
                or nx >= len(maze[0])
                or ny >= len(maze)
                or next_key in visited
                or maze[ny][nx] == "#"
            ):
                continue

            u_path_copy = u.path.copy()
            u_path_copy.add(f"{nx},{ny}")

            if u.dir != dd:
                heapq.heappush(
                    q, QueueNodeWithPath(u.dist + 1001, dd, nx, ny, u_path_copy)
                )
            else:
                heapq.heappush(
                    q, QueueNodeWithPath(u.dist + 1, dd, nx, ny, u_path_copy)
                )

    return len(paths_by_score[int(lowest)])


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 16")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
