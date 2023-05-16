from unittest import TestCase, main
from random import choices

from modules import functions
from modules.classes import Deck, Cards


def is_seq_true_data_gen():
    deck = Deck()
    hand1 = [deck[i * 4] for i in range(5)]
    hand2 = [deck[(i + 5) * 4] for i in range(5)]
    hand3 = [deck[(i + 6) * 4] for i in range(5)]
    hand4 = [deck[(i + 7) * 4] for i in range(5)]
    hand5 = [deck[(i + 8) * 4] for i in range(5)]
    hand6 = [Cards('A', '♣'), Cards('2', '♥'), Cards('3', '♥'), Cards('4', '♥'), Cards('5', '♥')]
    return [hand5, hand4, hand3, hand2, hand1, hand6]


def is_seq_false_data_gen():
    deck = [Cards(r, s) for r in Deck._rank_values for s in Deck._suits]
    hands = [choices(deck, k=5) for _ in range(5)]
    return hands


def is_suited_true_data_gen():
    deck = [Cards(r, s) for s in Deck._suits for r in Deck._rank_values][:13]
    hands = [choices(deck, k=5) for _ in range(5)]
    return hands


def is_suited_true_data_gen():
    deck = [Cards(r, s) for s in Deck._suits for r in Deck._rank_values][:13]
    hands = [choices(deck, k=5) for _ in range(5)]
    return hands


def is_suited_false_data_gen():
    deck = [Cards(r, s) for r in Deck._rank_values for s in Deck._suits]
    hands = [deck[i: i + 5] for i in range(0, 25, 5)]
    return hands


def test_straight_flush_true_gen():
    pass



class FunctionsTests(TestCase):

    def test_is_suited_true(self):
        for hand in is_suited_true_data_gen():
            self.assertIs(functions.is_flush(hand), True)  # add assertion here

    def test_is_suited_false(self):
        for hand in is_suited_false_data_gen():
            self.assertIs(functions.is_flush(hand), False)  # add assertion here

    def test_is_sequence_true(self):
        for hand in is_seq_true_data_gen():
            self.assertEqual(functions.is_straight(hand), True)

    def test_is_sequence_false(self):
        for hand in is_seq_false_data_gen():
            self.assertEqual(functions.is_straight(hand), False)

    def test_straight_flush_true(self):
        pass


if __name__ == '__main__':
    main()
