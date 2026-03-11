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

cards = [ "A", "2", "3", "4", "5", "6", "7", "8", "9", "10," "J", "K", "Q" ]
cards_values = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "K": 10,
    "Q": 10,
}

def draw_game():
    print(cards_values["A"])

draw_game()
