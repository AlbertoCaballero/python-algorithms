import random

# choose a random word
word_list = ["random", "word", "hangman"]
word = random.choice(word_list)
state = "_" * len(word)
turns = 6

# Replace the correctlly guessed elements in state and return the new state
def add_guess_to_state(letter):
    new_state = state
    if letter not in state:
        indexes = []
        for index, element in enumerate(word):
            if element == letter:
                indexes.append(index)
        for i in indexes:
            new_state = new_state[:i] + letter + new_state[i + 1:]
    return new_state

def ascii_graphic(t):
    hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']
    return hangman_pics[6-t]

# show user status of game
while state != word and turns != -1:
    print(f"{ascii_graphic(turns)}")
    print(f"\nWord: {state}")
    print(f"Turns left: {turns}")

    guess = input("\nGuess your letter: ").lower()

    if guess == word:
        print("Full match!")
        state = word

    if guess in word:
        print("Nice!")
        state = add_guess_to_state(guess)
    else:
        print("Nope")
        turns -= 1

    if state == word:
        print("Yes! You win!")
        print(f"The word was: {word}")

    if turns == -1:
        print("No! You lose!")
        print(f"The word was: {word}")

