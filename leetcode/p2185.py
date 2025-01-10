class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        return len([word for word in words if word.startswith(pref)])
