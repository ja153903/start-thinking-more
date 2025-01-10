from collections import Counter


class Solution:
    def wordSubsets(self, a: list[str], b: list[str]) -> list[str]:
        b = list(set(["".join(sorted(s)) for s in b]))
        result = []
        for s in a:
            if all(self.is_subset(s, t) for t in b):
                result.append(s)
        return result

    def is_subset(self, a: str, b: str) -> bool:
        if len(a) < len(b):
            return False

        cnt = Counter(a)

        for ch in b:
            if ch not in cnt:
                return False
            if cnt[ch] == 0:
                return False

            cnt[ch] -= 1

        return True
