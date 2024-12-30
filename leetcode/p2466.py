from functools import lru_cache


MOD = 10**9 + 7


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @lru_cache
        def inner(path: str) -> int:
            if len(path) > high:
                return 0

            res = 0

            if low <= len(path) <= high:
                res += 1

            return res + inner(path + "0" * zero) + inner(path + "1" * one)

        return inner("") % MOD
