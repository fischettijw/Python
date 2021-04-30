import random
random.seed(42)


def list_cards(lst):
    for itm in lst:
        print(itm)
    print('='*28)


def wins():
    print('='*48)
    print(f'Player 1 Wins": {wins_player1}')
    print(f'Player 2 Wins": {wins_player2}')
    # print(f'Computer Wins": {wins_computer}')
    # print(wins1)
    # print(wins2)
    # print(player1)
    # print(player2)


total_cards_in_deck = 52

# deck = list(range(1, 14))+list(range(1, 14)) + list(range(1, 14))+list(range(1, 14))
deck = list(range(1, total_cards_in_deck+1))
# total_cards_in_deck = len(deck)
random.shuffle(deck)

player1 = deck[:(total_cards_in_deck//2)]
player2 = deck[(total_cards_in_deck//2):]

wins_player1 = 0
wins_player2 = 0
wins_computer = 0

wins1 = []
wins2 = []
for i in range(total_cards_in_deck//2):
    # print(f'{i} \t Player 1: {player1[i]} \t Player 2: {player2[i]}', end='')
    if player1[i] > player2[i]:
        wins_player1 += 1
        # print(f' \t-  Player 1 WINS')
        wins1.append(player1[i])
    else:
        wins_player2 += 1
        # print(f' \t-  Player 2 WINS')
        wins2.append(player1[i])


print()

print('player1 - before', player1)
print('player2 - before', player2)
print()
print('wins1', wins1)
print('wins2', wins2)
print()
for i in wins2:
    player2.append(i)
    player1.remove(i)
print('player1 - after', player1)
print('player2 - after', player2)
print()

all_cards = player1 + player2
print(all_cards, len(all_cards))
print()
all_cards.sort()
print(all_cards, len(all_cards))


# print('wins1', wins1)
# for i in wins1:
#     player1.append(i)
#     player2.remove(i)
# print('player1 - after', player1)
# print('player2 - after', player2)

# wins()
