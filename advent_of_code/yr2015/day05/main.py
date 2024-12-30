import os

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        return f.read().strip().splitlines()


def get_vowel_count(word: str) -> int:
    return sum(1 if ch in "aeiou" else 0 for ch in word)


def has_rep_chars(word: str) -> bool:
    for i in range(1, len(word)):
        if word[i] == word[i - 1]:
            return True
    return False


def has_forbidden_char(word: str) -> bool:
    for i in range(1, len(word)):
        if word[i - 1] == "a" and word[i] == "b":
            return True
        if word[i - 1] == "c" and word[i] == "d":
            return True
        if word[i - 1] == "p" and word[i] == "q":
            return True
        if word[i - 1] == "x" and word[i] == "y":
            return True
    return False


def is_nice(word: str) -> bool:
    return (
        get_vowel_count(word) >= 3
        and has_rep_chars(word)
        and not has_forbidden_char(word)
    )


def part1():
    return sum(1 if is_nice(line) else 0 for line in parse_input())


def has_char_between(word: str) -> bool:
    for i in range(1, len(word) - 1):
        if word[i - 1] == word[i + 1]:
            return True

    return False


def has_pair_twice(word: str) -> bool:
    for i in range(1, len(word)):
        a, b = word[i - 1], word[i]

        for j in range(i + 1, len(word) - 1):
            c, d = word[j], word[j + 1]

            if a == c and b == d:
                return True
    return False


def is_nice_part2(word: str) -> bool:
    return has_pair_twice(word) and has_char_between(word)


def part2():
    return sum(1 if is_nice_part2(line) else 0 for line in parse_input())


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 05")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
