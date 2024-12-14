import os
import re
from typing import TypedDict
from collections import Counter


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"

if "data.in" in PATH_TO_FILE:
    Y_LIMIT = 103
    X_LIMIT = 101

    X_MIDPOINT = 50
    Y_MIDPOINT = 51
else:
    Y_LIMIT = 7
    X_LIMIT = 11

    X_MIDPOINT = 5
    Y_MIDPOINT = 3


class Robot(TypedDict):
    px: int
    py: int
    vx: int
    vy: int


# In this regex, we make sure to capture entries that can either be positive or negative
ROBOT_REGEX = re.compile(r"p=(?P<px>-?\d+),(?P<py>-?\d+) v=(?P<vx>-?\d+),(?P<vy>-?\d+)")


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        data: list[Robot] = []
        for i, line in enumerate(f.read().strip().split("\n")):
            match = ROBOT_REGEX.match(line)
            if match:
                data.append(
                    {
                        "px": int(match.group("px")),
                        "py": int(match.group("py")),
                        "vx": int(match.group("vx")),
                        "vy": int(match.group("vy")),
                    }
                )
            else:
                raise ValueError("Could not parse data correctly; check regex")
        return data


def get_grid():
    return [[0 for _ in range(X_LIMIT)] for _ in range(Y_LIMIT)]


def move_robot(robot: Robot, x: int, y: int) -> tuple[int, int]:
    vx, vy = robot["vx"], robot["vy"]

    nx = x + vx
    ny = y + vy

    if nx < 0:
        nx += X_LIMIT

    if ny < 0:
        ny += Y_LIMIT

    return (nx % X_LIMIT, ny % Y_LIMIT)


def determine_quadrant(row: int, col: int) -> str:
    match (row, col):
        case (r, c) if r < Y_MIDPOINT and c > X_MIDPOINT:
            return "I"
        case (r, c) if r < Y_MIDPOINT and c < X_MIDPOINT:
            return "II"
        case (r, c) if r > Y_MIDPOINT and c < X_MIDPOINT:
            return "III"
        case _:
            return "IV"


def part1():
    grid = get_grid()
    robots = parse_input()

    for robot in robots:
        grid[robot["py"]][robot["px"]] += 1

    for _ in range(100):
        for robot in robots:
            x, y = robot["px"], robot["py"]
            grid[y][x] -= 1

            nx, ny = move_robot(robot, x, y)

            robot["px"], robot["py"] = nx, ny
            grid[ny][nx] += 1

    count_by_quadrants = Counter()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 0 and i != Y_MIDPOINT and j != X_MIDPOINT:
                count_by_quadrants[determine_quadrant(i, j)] += grid[i][j]

    res = 1

    for count in count_by_quadrants.values():
        res *= count

    return res


def only_ones(grid: list[list[int]]):
    for row in grid:
        for col in row:
            if col > 1:
                return False

    return True


# The intuition for part 2 is that we'll get some sort of tree if
# all the robots are in their own independent positions
def part2():
    grid = get_grid()
    robots = parse_input()

    for robot in robots:
        grid[robot["py"]][robot["px"]] += 1

    iteration = 0

    while True:
        for robot in robots:
            x, y = robot["px"], robot["py"]
            grid[y][x] -= 1

            nx, ny = move_robot(robot, x, y)

            robot["px"], robot["py"] = nx, ny
            grid[ny][nx] += 1

        iteration += 1

        if only_ones(grid):
            return iteration


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 14")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
