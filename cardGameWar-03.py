import random
import copy
# random.seed(123)


def list_cards(lst):
    for itm in lst:
        print(itm)
    print('='*28)


total_cards_in_deck = 52
# deck = list(range(1, 14))+list(range(1, 14)) + list(range(1, 14))+list(range(1, 14))
deck = list(range(1, total_cards_in_deck+1))
random.shuffle(deck)

player1 = deck[:(total_cards_in_deck//2)]
player2 = deck[(total_cards_in_deck//2):]

print(f'player1: {player1}')
print(f'player2: {player2}')
print()

ply1 = copy.deepcopy(player1)
ply2 = copy.deepcopy(player2)


for i in range(total_cards_in_deck//2):
    print(
        f'{i} \t Player 1: {player1[i]} \t Player 2: {player2[i]} \t', end='')
    if player1[i] > player2[i]:
        ply1.append(player2[i])
        ply2.remove(player2[i])
        print(f'1 WINS')

    else:
        ply2.append(player1[i])
        ply1.remove(player1[i])
        print(f'2 WINS')

print()
print(f'ply1: {ply1}')
print(f'ply2: {ply2}')
