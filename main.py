# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for modules, files, tool windows, actions, and settings.
from random import choices
from modules.classes import Deck, Player
import modules.functions


def is_suited_true_data_gen():
    deck = [modules.classes.Cards(r, s) for s in modules.classes.Deck._suits for r in
            modules.classes.Deck._rank_values][:13]
    hands = [choices(deck, k=5) for _ in range(5)]
    return hands


def main():
    deck = Deck()
    player = Player()
    deck.shuffle_cards()
    deck.deal_hand(player)
    print(player.hand)

    pass


if __name__ == '__main__':
    main()
