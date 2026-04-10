#  Number Guessing Game
import random

# Difficulty constants
INSANE = 1
HARD = 5
NORMAL = 15
EASY = 100

print("WELCOME TO THE NUMBER GUESSING GAME")
difficulty = input("Difficulty Insane (I), Hard(H), Normal(N), Easy(E): ")
attempts = 0

match difficulty:
    case "I":
        attempts = INSANE
    case "H":
        attempts = HARD
    case "N":
        attempts = NORMAL
    case "E":
        attempts = EASY

random_number = random.randint(1, 100)
print(random_number)

print("I'm thinking of a number bethween 1 and 100")
while attempts != 0:
    print(f"Attempts: {attempts}")
    guess = int(input("Take a guess: "))
    attempts -= 1

    if guess == random_number:
        print("That's right!")
        attempts = 0
    elif guess > random_number:
        print("To high!")
    elif guess < random_number:
        print("To low!")

