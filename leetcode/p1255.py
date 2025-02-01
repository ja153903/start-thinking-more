from collections import Counter
import itertools


class Solution:
    def maxScoreWords(
        self, words: list[str], letters: list[str], score: list[int]
    ) -> int:
        score_by_word = {}
        for word in words:
            _score = 0
            for ch in word:
                _score += score[ord(ch) - 97]
            score_by_word[word] = _score

        res = 0

        def iter(lst: list[str]):
            for perm in itertools.permutations(lst):
                yield perm

        for permutation in iter(words):
            letter_count = Counter(letters)
            final_score = 0

            for word in permutation:
                word_count = Counter(word)
                _score = score_by_word[word]
                can_construct = True
                for ch, count in word_count.items():
                    if letter_count[ch] < count:
                        can_construct = False
                        break

                if can_construct:
                    final_score += _score
                    for ch, count in word_count.items():
                        letter_count[ch] -= count

            res = max(res, final_score)

        return res
