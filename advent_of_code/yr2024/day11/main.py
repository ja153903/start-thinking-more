import os
from collections import Counter

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return [int(x) for x in f.read().strip().split(" ")]


def blink(stones: Counter[int]) -> Counter[int]:
    new_state: Counter[int] = Counter()

    for stone, count in stones.items():
        if stone == 0:
            new_state[1] += count
        elif len(as_str := str(stone)) % 2 == 0:
            left, right = int(as_str[: len(as_str) // 2]), int(
                as_str[len(as_str) // 2 :]
            )
            new_state[left] += count
            new_state[right] += count
        else:
            new_state[stone * 2024] += count

    return new_state


def part1():
    stones = Counter(parse_input())

    for _ in range(25):
        stones = blink(stones)

    return sum(stones.values())


def part2():
    stones = Counter(parse_input())

    for _ in range(75):
        stones = blink(stones)

    return sum(stones.values())


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 11")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
