import hashlib

INPUT = "iwrupvqb"


def part1():
    i = 1

    while True:
        input_string = f"{INPUT}{i}"
        input_bytes = input_string.encode("utf-8")
        m = hashlib.md5()
        m.update(input_bytes)
        if m.hexdigest().startswith("00000"):
            return i
        i += 1


def part2():
    i = 1

    m = hashlib.md5()

    while True:
        input_string = f"{INPUT}{i}"
        input_bytes = input_string.encode("utf-8")
        m = hashlib.md5()
        m.update(input_bytes)
        if m.hexdigest().startswith("000000"):
            return i
        i += 1


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 4")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
