import os

def clear_console():
    # Check the operating system
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux (Unix-like systems)
        os.system('clear')

def winner(all_bids):
    winner_name = ""
    winner_bid = 0
    for name in all_bids:
        if all_bids[name] > winner_bid:
            winner_bid = all_bids[name]
            winner_name = name
    return winner_name, winner_bid

clear_console()
print("SECRET BID PROGRAM")

bidders = {}
more_bidders = "yes"

while more_bidders != "no":
    name = input("Type bidders name: ")
    bid = int(input("Type bid: $"))
    bidders[name] = bid

    more_bidders = input("Are there more bidders? yes/no: ")
    clear_console()

    if more_bidders == "no":
        name, bid = winner(bidders) 
        print(f"\nCongratulations to {name}, and thanks for those ${bid}")

