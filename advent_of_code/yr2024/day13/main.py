import os
import re
import numpy as np


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


BUTTON_A_REGEX = re.compile(r"Button A: X\+(?P<ax>\d+), Y\+(?P<ay>\d+)")
BUTTON_B_REGEX = re.compile(r"Button B: X\+(?P<bx>\d+), Y\+(?P<by>\d+)")
PRIZE_REGEX = re.compile(r"Prize: X=(?P<px>\d+), Y=(?P<py>\d+)")


def parse_input(prize_increase: int = 0):
    with open(PATH_TO_FILE, "r") as f:
        data = f.read().strip().split("\n\n")

        equations = []

        for line in data:
            a, b, p = line.split("\n")

            a_btn = BUTTON_A_REGEX.match(a)
            b_btn = BUTTON_B_REGEX.match(b)
            prize = PRIZE_REGEX.match(p)

            if a_btn and b_btn and prize:
                equations.append(
                    {
                        "a": np.array(
                            [
                                [int(a_btn.group("ax")), int(b_btn.group("bx"))],
                                [int(a_btn.group("ay")), int(b_btn.group("by"))],
                            ]
                        ),
                        "b": np.array(
                            [
                                int(prize.group("px")) + prize_increase,
                                int(prize.group("py")) + prize_increase,
                            ]
                        ),
                    }
                )
            else:
                raise ValueError("Parsed it incorrectly")

        return equations


def part1():
    equations = parse_input()

    res = 0

    for equation in equations:
        sol = np.linalg.solve(equation["a"], equation["b"])

        ax, bx = equation["a"][0]
        ay, by = equation["a"][1]
        px, py = equation["b"]

        a, b = sol
        a, b = round(a), round(b)

        px_approx = a * ax + b * bx
        py_approx = a * ay + b * by

        if px_approx == px and py_approx == py:
            res += a * 3 + b

    return res


PART2_PRIZE_INCREASE = 10_000_000_000_000


def part2():
    equations = parse_input(PART2_PRIZE_INCREASE)

    res = 0

    for equation in equations:
        sol = np.linalg.solve(equation["a"], equation["b"])

        ax, bx = equation["a"][0]
        ay, by = equation["a"][1]
        px, py = equation["b"]

        a, b = sol
        a, b = round(a), round(b)

        px_approx = a * ax + b * bx
        py_approx = a * ay + b * by

        if px_approx == px and py_approx == py:
            res += a * 3 + b

    return res


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 13")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
