#imports random module for random number generation 
import random

# empty variables to keep track of wins
user_wins = 0
ai_wins = 0
tied_game = 0
choices = {
    '1': 'paper',
    '2': 'rock',
    '3': 'scissors',
}


# while loop to keep the game running
while True:
    # asks user for input, sets value to lowercase, and if 'q' is entered, the game ends (break)
    user_input = input("Type '1' for paper, '2' for rock, '3' for scissors, or 'q' to quit: ").lower()
    if user_input == "q":
        break

    # checks if user input is valid, repeats loop if not valid
    if user_input not in choices:
        print("Please enter a valid input.")
        continue
        
    
    # generates random number between 1 and 3, sets ai_pick to the corresponding 'choices' value
    # paper = 1, rock = 2, scissors = 3
    random_number = random.randint(1, 3)
    user_pick = choices[user_input]
    ai_pick = choices[str(random_number)]
    print("You picked", user_pick + ".")
    print("AI picked", ai_pick + ".")

    # checks for tie conditions, adds 1 to tied_game if tie
    if user_pick == ai_pick:
        tied_game += 1
        print("It's a tie!")

    # checks for win conditions, adds 1 to user_wins if win
    elif user_input == '1' and ai_pick == 'rock':
        print("You win!")
        user_wins += 1
    elif user_input == '2' and ai_pick == 'scissors':
        print("You win!")
        user_wins += 1
    elif user_input == '3' and ai_pick == 'paper':
        print("You win!")
        user_wins += 1
    
    # if not a tie or win, then it's a loss, adds 1 to ai_wins
    else:
        print("You lose!")
        ai_wins += 1

# prints out the final score; user_wins, ai_wins, tied_game
print("You won", user_wins, "times.")
print("The AI won", ai_wins, "times.")
print("You tied with the AI", tied_game, "times.")