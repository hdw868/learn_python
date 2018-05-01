from collections import namedtuple
from random import shuffle

Card = namedtuple('Card', 'rank, suit')
ranks = list(str(n) for n in range(2, 11)) + list('JQKA')
suits = ['spades', 'diamonds', 'clubs', 'hearts']


class FrenchDeck(object):
    def __init__(self):
        self._cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def shuffle(self):
        shuffle(self._cards)


if __name__ == '__main__':
    deck = FrenchDeck()
    print(deck[0])
    print(len(deck))
    deck.shuffle()
    print(deck[0])
