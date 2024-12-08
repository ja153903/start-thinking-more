from collections import defaultdict
import os

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return [list(line.strip()) for line in f.readlines()]


def part1():
    grid = parse_input()
    rows = len(grid)
    cols = len(grid[0])
    antinodes = [["." for _ in range(cols)] for _ in range(rows)]

    m: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != ".":
                m[grid[row][col]].append((row, col))

    for antennas in m.values():
        for i in range(len(antennas)):
            for j in range(i + 1, len(antennas)):
                delta_row = antennas[j][0] - antennas[i][0]
                delta_col = antennas[j][1] - antennas[i][1]

                sr, sc = antennas[i]
                er, ec = antennas[j]

                nr, nc = sr - delta_row, sc - delta_col
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    antinodes[nr][nc] = "#"

                nr, nc = er + delta_row, ec + delta_col
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    antinodes[nr][nc] = "#"

    res = 0
    for row in range(rows):
        for col in range(cols):
            if antinodes[row][col] == "#":
                res += 1
    return res


def part2():
    grid = parse_input()
    rows = len(grid)
    cols = len(grid[0])
    antinodes = [["." for _ in range(cols)] for _ in range(rows)]

    m: defaultdict[str, list[tuple[int, int]]] = defaultdict(list)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != ".":
                m[grid[row][col]].append((row, col))

    for antennas in m.values():
        for i in range(len(antennas)):
            for j in range(i + 1, len(antennas)):
                delta_row = antennas[j][0] - antennas[i][0]
                delta_col = antennas[j][1] - antennas[i][1]

                sr, sc = antennas[i]
                er, ec = antennas[j]

                while 0 <= sr < len(grid) and 0 <= sc < len(grid[0]):
                    nr, nc = sr - delta_row, sc - delta_col
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        antinodes[nr][nc] = "#"
                    sr, sc = nr, nc

                while 0 <= er < len(grid) and 0 <= ec < len(grid[0]):
                    nr, nc = er + delta_row, ec + delta_col
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        antinodes[nr][nc] = "#"
                    er, ec = nr, nc

    res = 0
    for row in range(rows):
        for col in range(cols):
            if antinodes[row][col] == "#" or (
                grid[row][col] != "." and len(m[grid[row][col]]) > 1
            ):
                res += 1
    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 8")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
