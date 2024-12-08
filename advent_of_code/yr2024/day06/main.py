import os
from collections import Counter


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        lines = f.readlines()

        return [line.strip() for line in lines]


direction = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}


def turn_right(current_direction: str) -> str:
    match current_direction:
        case "^":
            return ">"
        case ">":
            return "v"
        case "v":
            return "<"
        case "<":
            return "^"
        case _:
            raise ValueError(f"Invalid direction: {current_direction}")


def part1() -> int:
    grid = parse_input()
    x, y = 0, 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                x, y = i, j
                break

    visited: set[tuple[int, int]] = set()

    current_direction = "^"
    visited.add((x, y))

    while 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        visited.add((x, y))

        next_direction = direction[current_direction]

        nx, ny = x + next_direction[0], y + next_direction[1]

        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
            break

        if grid[nx][ny] == "#":
            current_direction = turn_right(current_direction)
        else:
            x, y = nx, ny

    return len(visited)


# TODO: Figure out a smarter way to do this
# Currently, I just brute-forced it to figure out when we would likely be in an infinte loop
def part2():
    grid = parse_input()
    grid = [list(line) for line in grid]
    x, y = 0, 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^":
                x, y = i, j
                break

    visited: set[tuple[int, int]] = set()

    current_direction = "^"
    visited.add((x, y))

    cx, cy = x, y

    while 0 <= cx < len(grid) and 0 <= cy < len(grid[0]):
        visited.add((cx, cy))

        next_direction = direction[current_direction]

        nx, ny = cx + next_direction[0], cy + next_direction[1]

        if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
            break

        if grid[nx][ny] == "#":
            current_direction = turn_right(current_direction)
        else:
            cx, cy = nx, ny

    visited.remove((x, y))

    positions = 0

    for i, j in visited:
        visited_counter: Counter[tuple[int, int]] = Counter()

        temp = grid[i][j]
        grid[i][j] = "#"

        cx, cy = x, y
        current_direction = "^"

        while 0 <= cx < len(grid) and 0 <= cy < len(grid[0]):
            visited_counter[(cx, cy)] += 1

            next_direction = direction[current_direction]

            nx, ny = cx + next_direction[0], cy + next_direction[1]

            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]):
                break

            if grid[nx][ny] == "#":
                current_direction = turn_right(current_direction)

                # as a heuristic, we'll say that we're in an infinite loop
                # if we've turned at an obstacle 3 times
                if visited_counter[(cx, cy)] >= 3:
                    positions += 1
                    break
            else:
                cx, cy = nx, ny

        grid[i][j] = temp

    return positions


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 6")

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
