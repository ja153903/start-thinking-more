import os
import math
from typing import TypedDict


class Register(TypedDict):
    A: int
    B: int
    C: int


class Input(TypedDict):
    registers: Register
    program: list[int]


PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input() -> Input:
    with open(PATH_TO_FILE, "r") as f:
        data = f.read().strip()
        raw_regi, raw_prog = data.split("\n\n")

        registers: Register = {"A": 0, "B": 0, "C": 0}
        for line in raw_regi.split("\n"):
            _key, _value = line.split(": ")
            _, key = _key.split(" ")
            registers[key] = int(_value)

        _, _program = raw_prog.split(": ")
        program = [int(x) for x in _program.split(",")]

        return {"registers": registers, "program": program}


def get_combo_operand(registers: Register, operand: int):
    match operand:
        case operand if 0 <= operand <= 3:
            return operand
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]
        case _:
            raise ValueError("Not a valid program if 7 was passed as an operand")


def eval_opcode(registers: Register, operand: int, opcode: int):
    mut_ptr, mut_out = None, None

    match opcode:
        case 0:
            registers["A"] = math.trunc(
                registers["A"] / 2 ** get_combo_operand(registers, operand)
            )
        case 1:
            registers["B"] = registers["B"] ^ operand
        case 2:
            registers["B"] = get_combo_operand(registers, operand) % 8
        case 3:
            if registers["A"] != 0:
                mut_ptr = operand
        case 4:
            registers["B"] = registers["B"] ^ registers["C"]
        case 5:
            mut_out = get_combo_operand(registers, operand) % 8
        case 6:
            registers["B"] = math.trunc(
                registers["A"] / 2 ** get_combo_operand(registers, operand)
            )
        case 7:
            registers["C"] = math.trunc(
                registers["A"] / 2 ** get_combo_operand(registers, operand)
            )
        case _:
            raise ValueError("Invalid opcode provided")

    return mut_ptr, mut_out


def get_output(registers: Register, program: list[int]):
    result = []
    ptr = 0

    while ptr < len(program) - 1:
        opcode = program[ptr]
        operand = program[ptr + 1]

        mut_ptr, mut_out = eval_opcode(registers, operand, opcode)

        if mut_ptr is not None:
            ptr = mut_ptr
            continue

        if mut_out is not None:
            result.append(mut_out)

        ptr += 2

    return ",".join([str(x) for x in result])


def part1():
    params = parse_input()
    registers = params["registers"]
    program = params["program"]

    return get_output(registers, program)


def part2():
    params = parse_input()
    registers = params["registers"]
    program = params["program"]

    quine = ",".join([str(x) for x in program])

    starts = [0]

    while True:
        candidates = []
        for a in starts:
            for a_test in range(a, a + 8):
                register_copy = registers.copy()
                register_copy["A"] = a_test
                out = get_output(register_copy, program)

                if out == quine[len(quine) - len(out) :]:
                    if out == quine:
                        return a_test
                    else:
                        candidates.append(a_test)

        starts = [x << 3 for x in candidates]


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 17")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
