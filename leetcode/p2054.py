class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        """
        Choose up to two events that don't overlap
        such that their sum is maximized

        the simple solution here is to go through all events in O(n^2) time
        and just pick the two events that have the maximum sum
        """
        max_sum = 0

        events.sort(key=lambda e: e[0])

        for i in range(len(events)):
            current_sum = events[i][2]
            max_current_sum = current_sum

            # can we make this part at least O(log n) instead
            # instead of this being O(n)

            for j in range(i + 1, len(events)):
                if events[j][0] > events[i][1]:
                    max_current_sum = max(max_current_sum, current_sum + events[j][2])

            max_sum = max(max_sum, max_current_sum)

        return max_sum
