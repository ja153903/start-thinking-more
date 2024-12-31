import os
import heapq
from typing import NamedTuple
from collections import defaultdict

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


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

    dd = defaultdict(lambda: float("inf"))
    dd[start] = 0

    while q:
        dist, x, y = heapq.heappop(q)

        if (x, y) == end:
            return dist

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if (
                nx < 0
                or ny < 0
                or nx >= len(maze[0])
                or ny >= len(maze)
                or maze[ny][nx] == "#"
            ):
                continue

            alt = dist + 1
            if alt <= dd[(nx, ny)]:
                dd[(nx, ny)] = alt
                heapq.heappush(q, RegularNode(alt, nx, ny))

    raise ValueError("Could not find the optimal path")


def part1():
    maze = parse_input()
    picosecond_without_cheats = dijkstras(maze)

    res = 0

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == "#":
                maze[y][x] = "."
                picoseconds = dijkstras(maze)
                try:
                    if picosecond_without_cheats - picoseconds >= 100:
                        res += 1
                except ValueError:
                    pass
                maze[y][x] = "#"

    return res


def dijkstras_from_point(maze: list[list[str]], start: tuple[int, int]):
    q: list[RegularNode] = []
    heapq.heappush(q, RegularNode(0, start[0], start[1]))

    dd = defaultdict(lambda: float("inf"))
    dd[start] = 0

    while q:
        dist, x, y = heapq.heappop(q)

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if (
                nx < 0
                or ny < 0
                or nx >= len(maze[0])
                or ny >= len(maze)
                or maze[ny][nx] == "#"
            ):
                continue

            alt = dist + 1
            if alt <= dd[(nx, ny)]:
                dd[(nx, ny)] = alt
                heapq.heappush(q, RegularNode(alt, nx, ny))

    return dd


def part2():
    """
    The idea with this solution is to find all the distances from the start to every point
    and also to find the distances from the end to every point

    With this information, we can find out if its possible to reach any two points
    within 20 cheats.

    Then we should check if (S -> A) + (A -> B) + (B -> E) will be less than the
    optimal answer - 100
    """
    maze = parse_input()
    start, end = find_start_and_end_points(maze)
    dd_from_start = dijkstras_from_point(maze, start)
    dd_from_end = dijkstras_from_point(maze, end)

    res = 0

    for x, y in dd_from_start.keys():
        for nx, ny in dd_from_end.keys():
            if (diff := abs(nx - x) + abs(ny - y)) <= 20:
                if (
                    dd_from_start[(x, y)] + diff + dd_from_end[(nx, ny)]
                    <= dd_from_start[end] - 100
                ):
                    res += 1

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 20")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
