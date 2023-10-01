#! /usr/bin/env python3 

import random
from typing import Any, List

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds',)
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', 
            '7', '8', '9', '10', 'Jack', 'Queen', 'King',)
N_CARDS = 8 


def get_card(deck_list_in: List[str]) -> str:
    """Pass in a deck and this function
        returns a random card from the deck.
    """

    this_card = deck_list_in.pop()
    return this_card


def shuffle(deck_list_in: List[Any]) -> List[Any]:
    """Pass in a deck and this function returns 
        a shuffled copy of the deck.
    """

    deck_list_out = deck_list_in.copy()
    random.shuffle(deck_list_out)
    return deck_list_out


def main():

    print('Welcome to Higher or Lower.')
    print('You have to choose whether the next card to be shown wil be higher or lower')
    print('Getting it right adds 20 points.')
    print('Get it wrong and you lose 15 points.')
    print('You have 5o points to start.')
    print()

    start_deck_list = []
    for suit in SUIT_TUPLE:
        for this_value, rank in enumerate(RANK_TUPLE):
            card_dict = {
                'rank': rank, 
                'suit': suit, 
                'value': this_value + 1,
            } 
            start_deck_list.append(card_dict)

    score = 150 
    while True:
        # Play multiple games.

        print()
        game_deck_list = shuffle(start_deck_list)
        current_card_dict = get_card(game_deck_list)
        current_card_rank = current_card_dict['rank']
        current_card_value = current_card_dict['value']
        current_card_suit = current_card_dict['suit']

        print(f"""Starting card is -> {current_card_rank} 
                                of -> {current_card_suit}""")
        print()

        for card_number in range(0, N_CARDS):
            """Play one game of this many cards"""

            message = f"""will the next card be higher or 
                        lower than the {current_card_rank} 
                        of {current_card_suit}? (enter h or l) -> """

            answer = input(message)
            answer = answer.casefold()
            next_card_dict = get_card(game_deck_list)
            next_card_rank = next_card_dict['rank']
            next_card_suit = next_card_dict['suit']
            next_card_value = next_card_dict['value']

            print(f'Next card is {next_card_rank} of {next_card_suit}')

            if answer == 'h':
                if next_card_value > current_card_value:
                    print('You got it right, it was higher.')
                    score = score + 20 
                else:
                    print('Sorry, it was not higher')
                    score = score - 15
            elif answer == 'l':
                if next_card_value < current_card_value:
                    score = score + 20
                    print('You got it right, it was lower')
                else:
                    score = score - 15
                    print('Sorry, it was not lower')
            print(f'Yor score -> {score}')
            print()

            current_card_rank = next_card_rank
            current_card_value = next_card_value
            current_card_suit = next_card_suit

        message_again = 'To play again, press Enter, or "q" to quit -> '
        go_again = input(message_again)
        if go_again == 'q':
            break
    print('Bye')

if __name__ == '__main__':
    main()