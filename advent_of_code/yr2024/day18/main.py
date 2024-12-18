import os
import heapq
from typing import NamedTuple


class Node(NamedTuple):
    dist: int
    x: int
    y: int


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        data = f.read().strip()
        fbytes = []
        for line in data.split("\n"):
            x, y = [int(x) for x in line.split(",")]
            fbytes.append((x, y))
        return fbytes


DIRECTIONS = ((1, 0), (-1, 0), (0, -1), (0, 1))


def part1():
    falling_bytes = parse_input()
    grid = [["." for _ in range(71)] for _ in range(71)]
    ex, ey = len(grid[0]) - 1, len(grid) - 1

    for i in range(1024):
        bx, by = falling_bytes[i]
        grid[by][bx] = "#"

    q: list[Node] = [Node(0, 0, 0)]

    visited = set()

    while q:
        u = heapq.heappop(q)

        if u.x == ex and u.y == ey:
            return u.dist

        if (u.x, u.y) in visited:
            continue

        visited.add((u.x, u.y))

        for dx, dy in DIRECTIONS:
            nx, ny = u.x + dx, u.y + dy

            if (
                0 <= nx < len(grid[0])
                and 0 <= ny < len(grid)
                and grid[ny][nx] != "#"
                and (nx, ny) not in visited
            ):
                heapq.heappush(q, Node(u.dist + 1, nx, ny))


def dijkstra(grid: list[list[str]]):
    ex, ey = len(grid[0]) - 1, len(grid) - 1

    q: list[Node] = [Node(0, 0, 0)]

    visited = set()

    while q:
        u = heapq.heappop(q)

        if u.x == ex and u.y == ey:
            return u.dist

        if (u.x, u.y) in visited:
            continue

        visited.add((u.x, u.y))

        for dx, dy in DIRECTIONS:
            nx, ny = u.x + dx, u.y + dy

            if (
                0 <= nx < len(grid[0])
                and 0 <= ny < len(grid)
                and grid[ny][nx] != "#"
                and (nx, ny) not in visited
            ):
                heapq.heappush(q, Node(u.dist + 1, nx, ny))

    return None


def part2():
    falling_bytes = parse_input()
    grid = [["." for _ in range(71)] for _ in range(71)]

    for i, fbyte in enumerate(falling_bytes):
        bx, by = fbyte
        grid[by][bx] = "#"

        if i < 1024:
            continue

        if dijkstra(grid) is None:
            return f"{bx},{by}"


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 18")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
