
#The computer randomly chooses a number between 1 and 100. 
# The player has to guess the number.After each guess, the game should give hints like "Too High" or "Too Low".
#The game ends when the player guesses correctly, and it should display the number of attempts.
#Use functions to organize the code, and include error handling for invalid inputs.

import random   

def guess_game():
    number_to_guess = random.randint(1, 100) 
    attempts = 0

    while True:
        user_input = input("Enter your guess (between 1 and 100 or type 'exit' to quit): ")

        # check if user wants to quit
        if user_input.lower() in ["exit", "quit"]:
            print("You exited the game. Thanks for playing!")
            break  

        try:
            guess = int(user_input)

            if guess < 1 or guess > 100:
                print(" Please enter a number within the range of 1 to 100.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print("Too Low!")
            elif guess > number_to_guess:
                print("Too High!")
            else:
                print(f" Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break

        except ValueError:
            print(" Invalid input. Please enter a valid integer or type 'exit'.")

print("----GUESS THE NUMBER GAME----")
print("You have to guess a number between 1 and 100.")
print("After each guess, you'll receive hints like 'Too High' or 'Too Low'.")
print("Type 'exit' anytime to quit the game.")
print("The game ends when you guess correctly, and it will display the number of attempts.\n")
guess_game()
