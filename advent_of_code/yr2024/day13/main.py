import os
import re
import numpy as np
import numpy.typing as npt


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


def compute_tokens_consumed(
    eq_a: npt.NDArray[np.int_], eq_b: npt.NDArray[np.int_]
) -> int:
    sol = np.linalg.solve(eq_a, eq_b)

    ax, bx = eq_a[0]
    ay, by = eq_a[1]
    px, py = eq_b

    a, b = sol
    a, b = round(a), round(b)

    px_approx = a * ax + b * bx
    py_approx = a * ay + b * by

    if px_approx == px and py_approx == py:
        return a * 3 + b

    return 0


def part1():
    equations = parse_input()
    return sum(compute_tokens_consumed(eq["a"], eq["b"]) for eq in equations)


PART2_PRIZE_INCREASE = 10_000_000_000_000


def part2():
    equations = parse_input(PART2_PRIZE_INCREASE)
    return sum(compute_tokens_consumed(eq["a"], eq["b"]) for eq in equations)


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 13")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
