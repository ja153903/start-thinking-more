class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        result = []

        for word in words:
            for another_word in words:
                if word != another_word and word in another_word:
                    result.append(word)
                    break

        return result
