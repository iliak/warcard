#!/usr/bin/python3

from random import shuffle

PlayerA = object()
PlayerB = object()


def generate_deck():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

    deck = [x % 13 + 1 for x in range(52)]
    shuffle(deck)

    return deck


def compare(playera, playerb, stash):

    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '1': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    card_a = stash[-1]
    card_b = stash[-2]

    if card_a > card_b:
        return PlayerA
    elif card_a < card_b:
        return PlayerB
    else:
        try:
            stash.append(playera.pop())
            stash.append(playerb.pop())
            stash.append(playera.pop())
            stash.append(playerb.pop())

            return compare(playera, playerb, stash)

        except IndexError:
            if playera:
                return PlayerA
            else:
                return PlayerB


def deal(deck):

    playerA = []
    playerB = []

    while deck:
        playerA.append(deck.pop())
        playerB.append(deck.pop())

    return playerA, playerB


def run():

    deck = generate_deck()
    playerA, playerB = deal(deck)

    rounds = 0
    while playerA and playerB:

        stash = [playerA.pop(),  playerB.pop()]
        if compare(playerA, playerB, stash) == PlayerA:
            playerA.extend(stash)
        else:
            playerB.extend(stash)

        rounds += 1

    i = 1


if __name__ == "__main__":
    while True:
        run()
