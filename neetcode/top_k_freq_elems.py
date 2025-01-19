from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        result = []
        for key, _value in counts.most_common(k):
            result.append(key)
        return result
