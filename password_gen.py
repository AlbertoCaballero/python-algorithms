import random
from functools import reduce

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pyssword Generator!")
nr_letters = int(input("Letters: "))
nr_numbers = int(input("Numbers: "))
nr_symbols = int(input("Symbols: "))

nr_total = nr_letters + nr_numbers + nr_symbols
password_array = []

for character in range(0, nr_total):
    new_char = ""

    while new_char == "":
        match random.randint(0, 3):
            case 0:
                if nr_letters > 0:
                    new_char = random.choice(letters)
                    nr_letters -= 1
            case 1:
                if nr_numbers > 0:
                    new_char = random.choice(numbers)
                    nr_numbers -= 1
            case 2:
                if nr_symbols > 0:
                    new_char = random.choice(symbols)
                    nr_symbols -= 1

    password_array.append(new_char)

print("\n\nPassword: " + reduce(lambda x, y: x + y, password_array))

