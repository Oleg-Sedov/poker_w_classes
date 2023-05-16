from random import shuffle, choices

from modules import settings


class ExceptionHandler:
    pass


class Deck:
    _rank_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9,
                    '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}  # ranks of cards
    _suits = ('♠', '♣', '♥', '♦')

    def __init__(self):
        self.card_deck = [Cards(rank, suit) for rank in Deck._rank_values for suit in Deck._suits]  # Contains Cards
        # instances

    def __len__(self):
        return len(self.card_deck)

    def __repr__(self):
        return f'{self.card_deck}]'

    def __getitem__(self, item: int):
        if 0 > item > len(self.card_deck):
            raise IndexError
        return self.card_deck[item]

    def show_deck(self):
        return [card.name for card in self.card_deck]

    def shuffle_cards(self) -> None:
        shuffle(self.card_deck)

    def deal_hand(self, player):
        if not isinstance(player.hand, list):
            player.hand = list()
        while len(player.hand) < 5:
            player.hand.append(self.card_deck.pop(0))


class Cards:

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.name = rank + suit
        self.rank_value = Deck._rank_values[rank]

    def __repr__(self):
        return self.name


class Player:
    combinations_payout_rates = settings.comb_pay_rates
    combinations = combinations_payout_rates.keys()

    def __init__(self, hand =None, points=settings.start_points, bet=0):
        self.hand = hand
        self.points = points
        self.bet = bet

    def drop_cards(self, dropped_cards: list) -> None:
        pass

    def get_hand(self):
        return f"Your hand is {' '.join(self.hand)}"

    def show_points(self):
        return f'You have {self.points} points'


if __name__ == '__main__':
    # raise RuntimeError('Only use as module')
    pass
