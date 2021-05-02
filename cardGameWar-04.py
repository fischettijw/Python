import random
import copy
# random.seed(123)


def list_cards(lst):
    for itm in lst:
        print(itm)
    print('='*28)


end_wins = 0
total_cards_in_deck = 52
deck = list(range(1, total_cards_in_deck+1))
random.shuffle(deck)
player1 = deck[:(total_cards_in_deck//2)]
player2 = deck[(total_cards_in_deck//2):]

num_of_games = 0

while min(len(player1), len(player2)) > end_wins:
    num_of_games += 1
    print(f'player1: {player1}')
    print(f'player2: {player2}')
    print()

    ply1 = copy.deepcopy(player1)
    ply2 = copy.deepcopy(player2)
    wins1 = 0
    wins2 = 0

    for i in range(min(len(player1), len(player2))):
        print(
            f'{i} \t Player 1: {player1[i]} \t Player 2: {player2[i]} \t \t', end='')
        if player1[i] > player2[i]:
            ply1.append(player2[i])
            ply2.remove(player2[i])
            wins1 += 1
            print(f'Player 1 WINS')
        else:
            ply2.append(player1[i])
            ply1.remove(player1[i])
            wins2 += 1
            print(f'Player 2 WINS')

    print()
    print(f'Player 1 WINS: {wins1} \t Player 2 Wins: {wins2}')

    print()
    print(f'ply1: {ply1}')
    print(f'ply2: {ply2}')

    player1 = copy.deepcopy(ply1)
    player2 = copy.deepcopy(ply2)

print()
print(f'Numbef of games: {num_of_games}')
