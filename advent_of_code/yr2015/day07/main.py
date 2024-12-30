import os
import re
from collections import defaultdict, deque
from enum import Enum
from typing import TypedDict


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return f.read().strip().splitlines()


class Operation(Enum):
    ASSIGN = 1
    NOT = 2
    AND = 3
    OR = -4
    RSHIFT = 5
    LSHIFT = 6


class Instruction(TypedDict):
    operation: Operation
    lhs: str
    rhs: str | None
    register: str


ASSIGNMENT_OPERATION_REGEX = re.compile(r"(\w+) -> (\w+)")
NOT_OPERATION_REGEX = re.compile(r"NOT (\w+) -> (\w+)")
OTHER_OPERATION_REGEX = re.compile(r"(\w+) (AND|OR|RSHIFT|LSHIFT) (\w+) -> (\w+)")


def get_operation(operation: str) -> Operation:
    match operation:
        case "AND":
            return Operation.AND
        case "OR":
            return Operation.OR
        case "RSHIFT":
            return Operation.RSHIFT
        case "LSHIFT":
            return Operation.LSHIFT
        case _:
            raise ValueError("Not a valid operation to get")


def parse_instruction(line: str) -> Instruction:
    if re.match(ASSIGNMENT_OPERATION_REGEX, line):
        lhs, register = [
            part for part in re.split(ASSIGNMENT_OPERATION_REGEX, line) if part
        ]
        return {
            "operation": Operation.ASSIGN,
            "lhs": lhs,
            "rhs": None,
            "register": register,
        }

    if re.match(NOT_OPERATION_REGEX, line):
        lhs, register = [part for part in re.split(NOT_OPERATION_REGEX, line) if part]
        return {
            "operation": Operation.NOT,
            "lhs": lhs,
            "rhs": None,
            "register": register,
        }

    if re.match(OTHER_OPERATION_REGEX, line):
        lhs, operation, rhs, register = [
            part for part in re.split(OTHER_OPERATION_REGEX, line) if part
        ]
        return {
            "operation": get_operation(operation),
            "lhs": lhs,
            "rhs": rhs,
            "register": register,
        }

    raise ValueError("Could not parse instruction properly")


def part1():
    dd = defaultdict(int)
    instructions = deque([parse_instruction(line) for line in parse_input()])

    while instructions:
        instruction = instructions.popleft()
        match instruction["operation"]:
            case Operation.ASSIGN:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    dd[instruction["register"]] = int(lhs)
                elif lhs in dd:
                    dd[instruction["register"]] = dd[lhs]
                else:
                    instructions.append(instruction)
            case Operation.NOT:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    dd[instruction["register"]] = ~int(lhs)
                elif lhs in dd:
                    dd[instruction["register"]] = ~dd[lhs]
                else:
                    instructions.append(instruction)
            case Operation.AND:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    lhs = int(lhs)
                elif lhs in dd:
                    lhs = dd[lhs]
                else:
                    instructions.append(instruction)
                    continue

                rhs = instruction["rhs"]
                if rhs and rhs.isdigit():
                    rhs = int(rhs)
                elif rhs in dd:
                    rhs = dd[rhs]
                else:
                    instructions.append(instruction)
                    continue

                dd[instruction["register"]] = lhs & rhs
            case Operation.OR:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    lhs = int(lhs)
                elif lhs in dd:
                    lhs = dd[lhs]
                else:
                    instructions.append(instruction)
                    continue

                rhs = instruction["rhs"]
                if rhs and rhs.isdigit():
                    rhs = int(rhs)
                elif rhs in dd:
                    rhs = dd[rhs]
                else:
                    instructions.append(instruction)
                    continue

                dd[instruction["register"]] = lhs | rhs
            case Operation.RSHIFT:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    lhs = int(lhs)
                elif lhs in dd:
                    lhs = dd[lhs]
                else:
                    instructions.append(instruction)
                    continue

                rhs = instruction["rhs"]
                if rhs and rhs.isdigit():
                    rhs = int(rhs)
                elif rhs in dd:
                    rhs = dd[rhs]
                else:
                    instructions.append(instruction)
                    continue

                dd[instruction["register"]] = lhs >> rhs
            case Operation.LSHIFT:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    lhs = int(lhs)
                elif lhs in dd:
                    lhs = dd[lhs]
                else:
                    instructions.append(instruction)
                    continue

                rhs = instruction["rhs"]
                if rhs and rhs.isdigit():
                    rhs = int(rhs)
                elif rhs in dd:
                    rhs = dd[rhs]
                else:
                    instructions.append(instruction)
                    continue

                dd[instruction["register"]] = lhs << rhs

    return dd["a"]


def part2():
    dd = defaultdict(int)
    instructions = [parse_instruction(line) for line in parse_input()]

    for i in range(len(instructions)):
        if instructions[i]["register"] == "b":
            instructions[i]["lhs"] = "46065"

    instructions = deque(instructions)

    while instructions:
        instruction = instructions.popleft()
        match instruction["operation"]:
            case Operation.ASSIGN:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    dd[instruction["register"]] = int(lhs)
                elif lhs in dd:
                    dd[instruction["register"]] = dd[lhs]
                else:
                    instructions.append(instruction)
            case Operation.NOT:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    dd[instruction["register"]] = ~int(lhs)
                elif lhs in dd:
                    dd[instruction["register"]] = ~dd[lhs]
                else:
                    instructions.append(instruction)
            case Operation.AND:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    lhs = int(lhs)
                elif lhs in dd:
                    lhs = dd[lhs]
                else:
                    instructions.append(instruction)
                    continue

                rhs = instruction["rhs"]
                if rhs and rhs.isdigit():
                    rhs = int(rhs)
                elif rhs in dd:
                    rhs = dd[rhs]
                else:
                    instructions.append(instruction)
                    continue

                dd[instruction["register"]] = lhs & rhs
            case Operation.OR:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    lhs = int(lhs)
                elif lhs in dd:
                    lhs = dd[lhs]
                else:
                    instructions.append(instruction)
                    continue

                rhs = instruction["rhs"]
                if rhs and rhs.isdigit():
                    rhs = int(rhs)
                elif rhs in dd:
                    rhs = dd[rhs]
                else:
                    instructions.append(instruction)
                    continue

                dd[instruction["register"]] = lhs | rhs
            case Operation.RSHIFT:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    lhs = int(lhs)
                elif lhs in dd:
                    lhs = dd[lhs]
                else:
                    instructions.append(instruction)
                    continue

                rhs = instruction["rhs"]
                if rhs and rhs.isdigit():
                    rhs = int(rhs)
                elif rhs in dd:
                    rhs = dd[rhs]
                else:
                    instructions.append(instruction)
                    continue

                dd[instruction["register"]] = lhs >> rhs
            case Operation.LSHIFT:
                lhs = instruction["lhs"]
                if lhs.isdigit():
                    lhs = int(lhs)
                elif lhs in dd:
                    lhs = dd[lhs]
                else:
                    instructions.append(instruction)
                    continue

                rhs = instruction["rhs"]
                if rhs and rhs.isdigit():
                    rhs = int(rhs)
                elif rhs in dd:
                    rhs = dd[rhs]
                else:
                    instructions.append(instruction)
                    continue

                dd[instruction["register"]] = lhs << rhs

    return dd["a"]


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 7")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
