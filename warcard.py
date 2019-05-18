#!/usr/bin/python3

from random import shuffle

PlayerA = object()
PlayerB = object()


def generate_deck():
    deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
    shuffle(deck)

    return deck


def compare(player_a, player_b, stash):

    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    card_a = stash[-1]
    card_b = stash[-2]

    if values[card_a] > values[card_b]:
        return PlayerA
    elif values[card_a] < values[card_b]:
        return PlayerB
    else:
        # Tie !
        try:
            stash.append(player_a.pop())
            stash.append(player_b.pop())
            stash.append(player_a.pop())
            stash.append(player_b.pop())

            return compare(player_a, player_b, stash)

        except IndexError:
            if player_a:
                return PlayerA
            else:
                return PlayerB


def deal(deck):

    player_a = []
    player_b = []

    while deck:
        player_a.append(deck.pop())
        player_b.append(deck.pop())

    return player_a, player_b


def run():

    deck = generate_deck()
    player_a, player_b = deal(deck)

    rounds = 0
    while player_a and player_b:

        stash = [player_a.pop(),  player_b.pop()]

        if compare(player_a, player_b, stash) == PlayerA:
            player_a.extend(stash)
        else:
            player_b.extend(stash)

        rounds += 1

    i = 1


if __name__ == "__main__":
    while True:
        run()
