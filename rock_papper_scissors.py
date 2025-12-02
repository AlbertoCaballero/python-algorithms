import random
import time

# ASCII Art for each choice
ROCK = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

PAPER = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

SCISSORS = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def get_ascii(choice):
    """Return ASCII art for the given choice"""
    if choice == 'rock':
        return ROCK
    elif choice == 'paper':
        return PAPER
    elif choice == 'scissors':
        return SCISSORS

def determine_winner(player, computer):
    """Determine the winner of the game"""
    if player == computer:
        return "It's a tie!"
    
    if (player == 'rock' and computer == 'scissors') or \
       (player == 'paper' and computer == 'rock') or \
       (player == 'scissors' and computer == 'paper'):
        return "You win! 🎉"
    else:
        return "Computer wins! 💻"

def play_game():
    """Main game loop"""
    print("\n" + "="*50)
    print("   ROCK PAPER SCISSORS GAME")
    print("="*50 + "\n")
    
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        print("\nChoose your weapon:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '4':
            print("\nThanks for playing! Goodbye! 👋\n")
            break
        
        if choice not in ['1', '2', '3']:
            print("\n❌ Invalid choice! Please enter 1, 2, 3, or 4.")
            continue
        
        # Map input to choice
        choice_map = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        player_choice = choice_map[choice]
        computer_choice = random.choice(choices)
        
        # Display choices with countdown
        print("\nRock...")
        time.sleep(0.5)
        print("Paper...")
        time.sleep(0.5)
        print("Scissors...")
        time.sleep(0.5)
        print("SHOOT!\n")
        
        # Show player choice
        print(f"You chose: {player_choice.upper()}")
        print(get_ascii(player_choice))
        
        # Show computer choice
        print(f"Computer chose: {computer_choice.upper()}")
        print(get_ascii(computer_choice))
        
        # Determine and display winner
        result = determine_winner(player_choice, computer_choice)
        print("\n" + "="*50)
        print(f"   {result}")
        print("="*50)

if __name__ == "__main__":
    play_game()

