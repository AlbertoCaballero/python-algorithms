import random

# choose a random word
word_list = ["random", "word", "hangman"]
word = random.choice(word_list)
state = "_" * len(word)
turns = 6
guessed_letters = set()

# Replace occurrences of `letter` in current_state using the target `word`
def add_guess_to_state(current_state, letter):
    new_state = list(current_state)
    for index, element in enumerate(word):
        if element == letter:
            new_state[index] = letter
    return "".join(new_state)

# Inserted: restore ASCII hangman art function
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
    return hangman_pics[6 - t]

# show user status of game
while state != word and turns > 0:
    print(ascii_graphic(turns))
    print(f"\nWord: {state}")
    print(f"Turns left: {turns}")
    if guessed_letters:
        print(f"Guessed: {', '.join(sorted(guessed_letters))}")

    guess = input("\nGuess your letter (or full word): ").lower().strip()
    if not guess:
        print("Please enter a letter or a word.")
        continue

    # Full-word correct guess
    if guess == word:
        state = word
        break

    # Single-letter guesses
    if len(guess) == 1:
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.add(guess)
        if guess in word:
            state = add_guess_to_state(state, guess)
            print("Nice!")
        else:
            print("Nope")
            turns -= 1
    else:
        # multi-letter wrong guess
        print("Nope")
        turns -= 1

# Final result
if state == word:
    print("Yes! You win!")
    print(f"The word was: {word}")
else:
    print(ascii_graphic(0))
    print("No! You lose!")
    print(f"The word was: {word}")

