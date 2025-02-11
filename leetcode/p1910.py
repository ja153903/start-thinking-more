class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """
        This is probably the intended solution from
        just a pure algorithmic POV
        """
        stack = []

        for ch in s:
            stack.append(ch)
            if len(stack) >= len(part) and "".join(stack[-len(part) :]) == part:
                for _ in range(len(part)):
                    stack.pop()

        return "".join(stack)
