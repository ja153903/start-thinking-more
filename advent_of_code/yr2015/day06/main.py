import os
import re
import numpy as np
from typing import NamedTuple, TypedDict
from enum import Enum

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return f.read().strip().splitlines()


class Command(Enum):
    TOGGLE = 1
    TURN_ON = 2
    TURN_OFF = 3


class Coordinate(NamedTuple):
    x: int
    y: int


class Instruction(TypedDict):
    command: Command
    start: Coordinate
    end: Coordinate


def parse_command(command: str) -> Command:
    match command:
        case "toggle":
            return Command.TOGGLE
        case "turn on":
            return Command.TURN_ON
        case "turn off":
            return Command.TURN_OFF
        case _:
            raise ValueError("Command does not exist")


def parse_instructions(line: str) -> Instruction:
    command, sx, sy, ex, ey = [
        part
        for part in re.split(
            r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)", line
        )
        if part
    ]

    return {
        "command": parse_command(command),
        "start": Coordinate(int(sx), int(sy)),
        "end": Coordinate(int(ex), int(ey)),
    }


def part1():
    instructions = [parse_instructions(line) for line in parse_input()]
    grid = np.zeros((1000, 1000), dtype=int)

    for instruction in instructions:
        start, end = instruction["start"], instruction["end"]

        match instruction["command"]:
            case Command.TOGGLE:
                grid[start.y : end.y + 1, start.x : end.x + 1] ^= 1
            case Command.TURN_ON:
                grid[start.y : end.y + 1, start.x : end.x + 1] = 1
            case Command.TURN_OFF:
                grid[start.y : end.y + 1, start.x : end.x + 1] = 0

    return grid.sum()


def part2():
    instructions = [parse_instructions(line) for line in parse_input()]
    grid = np.zeros((1000, 1000), dtype=int)

    for instruction in instructions:
        start, end = instruction["start"], instruction["end"]

        match instruction["command"]:
            case Command.TOGGLE:
                grid[start.y : end.y + 1, start.x : end.x + 1] += 2
            case Command.TURN_ON:
                grid[start.y : end.y + 1, start.x : end.x + 1] += 1
            case Command.TURN_OFF:
                for y in range(start.y, end.y + 1):
                    for x in range(start.x, end.x + 1):
                        grid[y, x] = max(0, grid[y, x] - 1)

    return grid.sum()


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 6")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
