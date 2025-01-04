from collections import defaultdict


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        dd = defaultdict(list)

        for i, ch in enumerate(s):
            dd[ch].append(i)

        res = 0

        for value in dd.values():
            if len(value) > 1:
                first, *_, last = value
                res += len(set(s[first + 1 : last]))

        return res
