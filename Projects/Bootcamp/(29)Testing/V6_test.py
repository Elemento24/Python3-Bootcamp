# repr() calls the dunder method __repr__()

import unittest
from V6_card import Card, Deck


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card('Hearts', 'A')

    def test_init(self):
        """Cards should have a Suit and a Value"""
        self.assertEqual(self.card.suit, 'Hearts')
        self.assertEqual(self.card.value, 'A')

    def test_repr(self):
        """repr should return a string of the form 'VALUE of SUIT'"""
        self.assertEqual(repr(self.card), 'A of Hearts')


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """Decks should have a cards attribute, which is a list of Cards"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertTrue(isinstance(self.deck.cards[0], Card))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """repr should return a string of the form 'Deck of COUNT cards'"""
        self.assertEqual(repr(self.deck), 'Deck of 52 cards')

    def test_count(self):
        """Count should return a count of cards in the Deck"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        """Deal should deal the number of cards specified, if available"""
        cards = self.deck._deal(5)
        self.assertEqual(len(cards), 5)
        self.assertEqual(self.deck.count(), 47)

    def test_deal_insufficient_cards(self):
        """If the number of cards to be dealt is insufficient, then it should deal all the remaining cards"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        """_deal should throw a ValueError, if the Deck is empty"""
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        """deal_card should deal one card from the deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertTrue(isinstance(dealt_card, Card))
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        """deal_hand should deal the number of cards specified"""
        cards = self.deck.deal_hand(20)
        self.assertTrue(isinstance(cards, list))
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        """Shuffle should shuffle the deck if the Deck is not full"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        self.deck.deal_card()
        with self.assertRaises(ValueError):
            self.deck.shuffle()


if __name__ == '__main__':
    unittest.main()
