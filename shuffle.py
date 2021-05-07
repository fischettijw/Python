# import os
# import random as rnd
# os.system('cls')

from random import randint, seed
seed()


def shuffle(deck, prnt=False):
    if prnt:
        print(sum(deck), deck)
    # print(sum(deck), deck) if prnt else print()  # None
    # print(sum(deck), deck) if prnt else None

    for i in range(len(deck)):
        deck[i] += (randint(1000, 10000) * 100)
    if prnt:
        print(deck)
    deck.sort()
    if prnt:
        print(deck)
    for i in range(len(deck)):
        deck[i] %= 100
    if prnt:
        print(sum(deck), deck)


a = [7, 2, 9, 35, 23, 97, 17, 1, 99]

shuffle(a, prnt=True)
