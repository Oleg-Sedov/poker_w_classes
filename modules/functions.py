"""
This module contains functions
"""
from collections import Counter
from modules.classes import *
from modules import settings


def show_payout_table():
    pass


def count_win(comb: str, bet: int) -> None:
    if comb not in settings.comb_pay_rates.keys():
        raise ValueError('Invalid combination. Not exist')

    return bet * settings.comb_pay_rates[comb]


def is_flush(hand: list) -> bool:
    for suite in (suites := [card.suit for card in hand]):  # проверка есть ли флэш
        if suite != suites[-1]:
            return False
    return True


def is_straight(hand: list) -> bool:
    hand.sort(key=lambda x: x.rank_value)
    if set([card.rank_value for card in hand]) == {14, 2, 3, 4, 5}:
        return True
    for i in range(len(hand) - 1):
        if hand[i].rank_value + 1 != hand[i + 1].rank_value:
            return False
    return True


def straight_flush(hand: list):
    return is_straight(hand) and is_flush(hand)


def check_combination(player) -> str:  # ToDo
    ranks_dict = settings.ranks
    ranks = sorted([ranks_dict.get(card.rank) for card in player.hand])

    rank_values = [card.rank_value for card in player.hand]
    ranks_count = Counter(rank_values)
    if max(ranks_count.values()) > 1:  # If max appearance number is less then 2 then there are no pairs in the hand
        match max(ranks_count.values()):
            case 2 if Counter(ranks_count.values())[2] == 2:
                """ We are in this case when the hand contains at least one repeated card (pair). The code below counts 
                how many cards have a pair (or counts pairs). ranks_count_.values() represents frequencies of cards 
                appearances. We are looking for how many cards appear 2 in the case, so we counts number of frequency 2.
                If frequency 2 appear once then there is one pair if twice then two pair. Other configurations 
                are not possible by argument. 
                """
                pass  # two pairs
            case 2:
                pass  # one pair
            case 3 if len(ranks_count) != 2:
                """ranks_counts contains dict of cards as keys with its appearance in the hand. If max appearance is 3 
                then we can have maximum three various cards in the hand. If len of ranks_count is not equal 2 then we 
                have three different card -> we have three of a kind. If len of ranks_count is equal 2 then we have 
                set of cards with appearance 3 and 2 then we have full house (next case).
                """
                pass  # set (three of a kind)
            case 3:
                pass  # full house
            case 4:
                pass  # Four of a kind


if __name__ == '__main__':
    pass

