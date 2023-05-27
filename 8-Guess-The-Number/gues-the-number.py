from random import randint
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer
def check_answer(guess, answer, turns) :
    """""Check answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess <answer :
        print("Too low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}")

#Make function to set difficuilty 
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    #Choosing a random number between 1 and 100
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    turns = set_difficulty()

    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempt remaining to guess the number.")
        #Let the user guess a number.
        guess = int(input("Make a guess: "))

        #Track the number of turns and reduce by 1 if they get it wrong answer
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of  guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()


  




# from random import randint
# import os
# random_number = randint(1, 100)

# def play_game():
#     print("Welcome to the Number Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#     difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

#     game_is_over = False
#     if difficulty_level == "hard":
#         print("You have 5 attempts remaning to guess the number.")
#         count = 5
#         while count > 0 and not game_is_over:
#             user_input = int(input("Make your guess: "))
#             if random_number == user_input:
#                 print("You made a correct guess")
#                 game_is_over = True
#             elif user_input > random_number:
#                 print("You went over")
#             elif user_input < random_number:
#                 print( "You went down")
#             else:
#                 print("Invalid input")
#             count -= 1
#     if difficulty_level == "easy":
#         print("You have 10 attempts remaning to guess the number.")
#         count = 10
#         while count > 0 and not game_is_over:
#             user_input = int(input("Make your guess: "))
#             if random_number == user_input:
#                 print("You made a correct guess")
#                 game_is_over = True
#             elif user_input > random_number:
#                 print("You went over")
#             elif user_input < random_number:
#                 print( "You went down")
#             else:
#                 print("Invalid input")
#             count -= 1

# while input("Do you want to play a game of Guessing number? Type 'y' or 'n': "):
#     os.system('cls') 
#     play_game()    

