import os

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE) as f:
        return f.read().strip()


def part1():
    path = parse_input()
    visited = set()

    x, y = 0, 0

    visited.add((x, y))

    for direction in path:
        match direction:
            case "^":
                visited.add((x, y - 1))
                y -= 1
            case "v":
                visited.add((x, y + 1))
                y += 1
            case "<":
                visited.add((x - 1, y))
                x -= 1
            case ">":
                visited.add((x + 1, y))
                x += 1
            case _:
                raise ValueError("Invalid direction provided")

    return len(visited)


def part2():
    path = parse_input()
    visited = set()

    x, y = 0, 0
    rx, ry = 0, 0

    visited.add((x, y))

    for i, direction in enumerate(path):
        match direction:
            case "^":
                if i % 2 == 0:
                    visited.add((x, y - 1))
                    y -= 1
                else:
                    visited.add((rx, ry - 1))
                    ry -= 1

            case "v":
                if i % 2 == 0:
                    visited.add((x, y + 1))
                    y += 1
                else:
                    visited.add((rx, ry + 1))
                    ry += 1
            case "<":
                if i % 2 == 0:
                    visited.add((x - 1, y))
                    x -= 1
                else:
                    visited.add((rx - 1, ry))
                    rx -= 1
            case ">":
                if i % 2 == 0:
                    visited.add((x + 1, y))
                    x += 1
                else:
                    visited.add((rx + 1, ry))
                    rx += 1
            case _:
                raise ValueError("Invalid direction provided")

    return len(visited)


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 3")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
