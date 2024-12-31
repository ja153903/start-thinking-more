INPUT = "3113322113"


def iter(line: str) -> str:
    res = []
    cur, count = line[0], 1

    for i in range(1, len(line)):
        if line[i] != cur:
            res.append(str(count))
            res.append(str(cur))
            cur, count = line[i], 1
        else:
            count += 1

    res.append(str(count))
    res.append(str(cur))

    return "".join(res)


def part1():
    digits = str(INPUT)
    for _ in range(40):
        digits = iter(digits)
    return len(digits)


def part2():
    digits = str(INPUT)
    for _ in range(50):
        digits = iter(digits)
    return len(digits)


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 10")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
