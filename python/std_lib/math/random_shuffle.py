#! /usr/bin/env python3 

import random
import itertools

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

def new_deck() -> list:
    return [
        # always use two position -> equally width strings 
        '{:>2}{}'.format(*c)
        for c in itertools.product(
            itertools.chain(range(2, 11), FACE_CARDS), 
            SUITS,
        )
    ]
    
def show_deck(deck: list) -> None:
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()
        
# create new deck with ordered cards 
deck = new_deck()
print('Initial deck -> ')
show_deck(deck)

# mix deck with function shuffle()
random.shuffle(deck)
print('\nShuffled deck -> ')
show_deck(deck)

# distribute cards on 4 handles on 5 cards on every handle
hands = [[], [], [], []]

for i in range(5):
    for h in hands:
        h.append(deck.pop())

# show distribute cards 
print('\nHands -> ') 
for n, h in enumerate(hands):
    print(f'{n + 1}', end=' ')
    for c in h:
        print(c, end=' ')
    print()
    
# show cards in remaminder (in deck)
print('\nReminding deck -> ')
show_deck(deck)