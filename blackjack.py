# Black Jack CLI game
# Goal of game, have cards that add up to the largest value without going over 21
#
# if more than 21: Bust -> Lose Game
#
# Number cards are face value
# J, Q, K are value 10
# A count as 1 or 11, player decides
#
# Dealer gets 1 card shown and 1 card hidden
# Player gets 2 cards
#
# Based on value, player asks for another card or just go down
# Then dealer and player shows cards
# Higher value wins
# If same value draw
#
# If dealer value less than 17, takes another card
#

import random

cards = [ "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q", ]
cards_values = { "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "K": 10, "Q": 10, }

player = []
dealer = []

def draw_random_card():
    return cards[random.randint(0, len(cards)-1)]

def count_total(game):
    # list(map(lambda x: cards_values[x], game))
    return sum([cards_values[card] for card in game])

def print_player(p):
    print(f"\nPlayer: {[f'{x}' for x in p]}")
    print(f"Total: {count_total(p)}\n")

def print_dealer(d, s):
    if not s:
        print(f"\nDealer: [{d[0] if s else "?"}, {d[1]}]")
        print(f"Total: {count_total(d) if s else "?"}\n")
    elif s:
        print(f"\nDealer: {d}")
        print(f"Total: {count_total(d)}\n")

def win_or_lose(d, p):
    d_total = count_total(d)
    p_total = count_total(p)

    if p_total > 21:
        print("===LOSE===")
    elif d_total > 21:
        print("===WIN===")
    elif d_total == p_total:
        print("===DRAW===")
    elif d_total > p_total:
        print("===LOSE===")
    elif d_total < p_total:
        print("===WIN===")


def game_loop():
    play = ""
    while True:
        print("==============================BLACK JACK==============================")
        play = input("You want to play Black Jack? Y/N\n")
        player = []
        dealer = []
        if play == "Y":
            print("DEAL!\n")

            player.append(draw_random_card())
            player.append(draw_random_card())

            dealer.append(draw_random_card())
            dealer.append(draw_random_card())

            print_dealer(dealer, False)
            print_player(player)

            more = input("Card or Fold? C/F\n")
            if more == "C":
                player.append(draw_random_card())

            if count_total(dealer) < 17:
                dealer.append(draw_random_card())

            print_dealer(dealer, True)
            print_player(player)
            win_or_lose(dealer, player)

        elif play == "N":
            break
        else:
            print("No valid option.\n")

    print("\nBYE")

game_loop()
