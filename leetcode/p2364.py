from collections import Counter


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        """
        O(n^2) => iterate over all possible combinations of (i, j) checking if j - i != nums[j] - nums[i]

        Another insight we should add here is that we might find it easier to calculate the number
        of good pairs and derive the number of bad pairs from the total number of pairs altogether
        """

        # This is too slow to solve this problem
        # bad_pairs = 0
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if j - i != nums[j] - nums[i]:
        #             bad_pairs += 1
        # return bad_pairs

        good_pairs, n = Counter(), len(nums)
        result = n * (n - 1) // 2

        for i, num in enumerate(nums):
            result -= good_pairs[num - i]
            good_pairs[num - i] += 1

        return result
