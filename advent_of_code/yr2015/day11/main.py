INPUT = "hxbxwxba"

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

alphabet_dict = {key: index for index, key in enumerate(ALPHABET)}
reverse_alphabet_dict = {index: key for index, key in enumerate(ALPHABET)}


def has_increasing_straight(password: str) -> bool:
    for i in range(2, len(password)):
        a, b, c = password[i - 2], password[i - 1], password[i]
        if (
            alphabet_dict[a] + 1 == alphabet_dict[b]
            and alphabet_dict[b] + 1 == alphabet_dict[c]
        ):
            return True
    return False


def has_confusing_letters(password: str) -> bool:
    return any(ch in password for ch in ("i", "o", "l"))


def get_count_of_nonoverlapping_pairs(password: str) -> int:
    pairs = []

    for i in range(len(password) - 1):
        if password[i] == password[i + 1]:
            pairs.append((i, i + 1, password[i]))

    if not pairs:
        return 0

    pairs.sort(key=lambda t: t[0])

    resulting_pairs = [pairs[0]]

    for i in range(1, len(pairs)):
        if pairs[i][0] < resulting_pairs[-1][1]:
            continue

        if resulting_pairs[-1][2] == pairs[i][2]:
            continue

        resulting_pairs.append(pairs[i])

    return len(resulting_pairs)


def is_valid_password(password: str) -> bool:
    return (
        has_increasing_straight(password)
        and not has_confusing_letters(password)
        and get_count_of_nonoverlapping_pairs(password) >= 2
    )


def increment_password(password: str) -> str:
    current = [alphabet_dict[ch] for ch in password[::-1]]

    carry = 0
    for i in range(len(current)):
        if i == 0 or carry > 0:
            current[i] += 1
            if current[i] >= 26:
                current[i] %= 26
                carry = 1
            else:
                carry = 0

    if carry > 0:
        current.append(carry)

    return "".join([reverse_alphabet_dict[ch] for ch in current[::-1]])


def part1():
    password = str(INPUT)
    while not is_valid_password(password):
        password = increment_password(password)
    return password


def part2():
    password = increment_password("hxbxxyzz")
    while not is_valid_password(password):
        password = increment_password(password)
    return password


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 11")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
