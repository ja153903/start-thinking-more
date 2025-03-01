from typing import LiteralString, NamedTuple


class Card(NamedTuple):
    rank: str
    suit: str


class FrenchDeck:
    ranks: list[str] = [str(n) for n in range(2, 11)] + list("JQKA")
    suits: list[LiteralString] = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards: list[Card] = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def __len__(self):
        return len(self._cards)

    # NOTE: Because __getitem__ delegates to the [] operator of self._cards
    # our deck automatically supports slicing.
    # By just implementing the __getitem__ special method, our deck is also iterable
    def __getitem__(self, position):
        return self._cards[position]

    # NOTE: if a collection has no __contains__ method, the in operator does a sequential scan
