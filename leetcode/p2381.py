ALPHABET = "abcdefghijklmnopqrstuvwxyz"


class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        chars = list(s)
        line_sweep = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            if direction == 1:
                line_sweep[start] += 1
                line_sweep[end + 1] -= 1
            else:
                line_sweep[start] -= 1
                line_sweep[end + 1] += 1

        for i in range(1, len(line_sweep)):
            line_sweep[i] += line_sweep[i - 1]

        for i, ch in enumerate(s):
            increase_by = (ALPHABET.index(ch) + line_sweep[i]) % 26
            increase_by = (increase_by + 26) % 26

            chars[i] = ALPHABET[increase_by]

        return "".join(chars)

    def shiftingLetters_tle(self, s: str, shifts: list[list[int]]) -> str:
        chars = list(s)

        for start, end, direction in shifts:
            delta = 1 if direction == 1 else -1

            for i in range(start, end + 1):
                char_idx = ALPHABET.index(chars[i]) + delta
                if char_idx < 0:
                    char_idx += len(ALPHABET)
                elif char_idx >= len(ALPHABET):
                    char_idx %= len(ALPHABET)

                chars[i] = ALPHABET[char_idx]

        return "".join(chars)
