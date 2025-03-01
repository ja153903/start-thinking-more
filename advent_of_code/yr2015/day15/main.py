from collections import defaultdict
import os
import re

PATH_TO_FILE = f"{os.path.dirname(os.path.realpath(__file__))}/data.in"

INGREDIENT_REGEX = r"(Sprinkles|PeanutButter|Frosting|Sugar|Butterscotch|Cinnamon): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"


def parse_input():
    with open(PATH_TO_FILE, "r") as f:
        lines = f.read().strip().splitlines()

        ingredients = []
        for line in lines:
            matches = re.split(INGREDIENT_REGEX, line)
            matches = [m for m in matches if m]
            _, capacity, durability, flavor, texture, calories = matches
            ingredients.append(
                {
                    "capacity": int(capacity),
                    "durability": int(durability),
                    "flavor": int(flavor),
                    "texture": int(texture),
                    "calories": int(calories),
                }
            )
        return ingredients


def generate_sum_permutations(n, k):
    def backtrack(remaining_sum, remaining_slots, current_perm):
        if remaining_slots == 0:
            if remaining_sum == 0:
                return [current_perm.copy()]
            return []

        if remaining_sum < remaining_slots or remaining_sum > remaining_slots * (
            k - sum(current_perm)
        ):
            return []

        result = []
        for i in range(1, remaining_sum - remaining_slots + 2):
            current_perm.append(i)
            result.extend(
                backtrack(remaining_sum - i, remaining_slots - 1, current_perm)
            )
            current_perm.pop()

        return result

    for permutation in backtrack(k, n, []):
        yield permutation


def part1():
    ingredients = parse_input()

    result = 0
    for permutation in generate_sum_permutations(len(ingredients), 100):
        current = defaultdict(int)
        for teaspoon, ingredient in zip(permutation, ingredients):
            for key, value in ingredient.items():
                current[key] += value * teaspoon

        if any(value < 0 for value in current.values()):
            continue

        product = 1
        for key, value in current.items():
            if key != "calories":
                product *= value

        result = max(result, product)

    return result


def part2():
    ingredients = parse_input()

    result = 0
    for permutation in generate_sum_permutations(len(ingredients), 100):
        current = defaultdict(int)
        for teaspoon, ingredient in zip(permutation, ingredients):
            for key, value in ingredient.items():
                current[key] += value * teaspoon

        if any(value < 0 for value in current.values()) or current["calories"] != 500:
            continue

        product = 1
        for key, value in current.items():
            if key != "calories":
                product *= value

        result = max(result, product)

    return result


if __name__ == "__main__":
    print("Advent of Code 2015 - Day 15")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
