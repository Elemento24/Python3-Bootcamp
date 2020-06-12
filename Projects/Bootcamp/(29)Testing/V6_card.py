from random import shuffle


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'


class Deck:

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(s, v) for s in suits for v in values]
        # for s in Deck.suits:
        #     for v in Deck.values:
        #         self.cards.append(Card(s, v))

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def _deal(self, num):
        # It stores the actual number of cards, we will be removing
        count = min([self.count(), num])
        if not self.count():
            raise ValueError('All cards have been dealt')
        cards = self.cards[-count:]
        self.cards = self.cards[:-count]
        return cards

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() != 52:
            raise ValueError('Only full decks can be shuffled')
        shuffle(self.cards)
        return self

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)
