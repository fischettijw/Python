import random


def list_cards(lst):
    for itm in lst:
        print(itm)
    print('='*28)


def wins():
    print('='*28)
    print(f'Player 1 Wins": {wins_player1}')
    print(f'Player 2 Wins": {wins_player2}')
    print(f'Computer Wins": {wins_computer}')


total_cards_in_deck = 52

# player1 = []
# player2 = []
# deck = list(range(1, 14))+list(range(1, 14)) + list(range(1, 14))+list(range(1, 14))
deck = list(range(1, total_cards_in_deck+1))
cards_in_deck = len(deck)
random.shuffle(deck)

player1 = deck[:(cards_in_deck//2)]
player2 = deck[(cards_in_deck//2):]
# list_cards(player1)
# list_cards(player2)

wins_player1 = 0
wins_player2 = 0
wins_computer = 0

for i in range(total_cards_in_deck//2):
    print(f'Player 1: {player1[i]}   Player 2: {player2[i]}')
    if player1[i] > player2[i]:
        wins_player1 += 1
    else:
        wins_player2 += 1

wins()
