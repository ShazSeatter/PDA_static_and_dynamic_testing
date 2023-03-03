import unittest
from src.card import Card
from src.card_game import CardGame 

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card = Card("Diamonds", 8)
        self.card2 = Card("Hearts", 1)
    
        self.cards = [self.card, self.card2]

        self.card_game = CardGame(self.cards)

    def test_check_for_ace__true(self):
        expected = True
        actual = self.card_game.check_for_ace(self.cards[1])
        self.assertEqual(expected, actual)

    def test_check_for_ace__false(self):
        expected = False
        actual = self.card_game.check_for_ace(self.cards[0])
        self.assertEqual(expected, actual)

    def test_highest_card(self):
        expected = 8
        actual = self.card_game.highest_card(self.card.value, self.card2.value)
        self.assertEqual(expected, actual)

    def test_cards_total(self):
        expected = "You have a total of 9"
        actual = self.card_game.cards_total(self.cards)
        self.assertEqual(expected, actual)
    

    