from Backend import *

def user_guess(): # takes the guesses
    guess = input("")
    return guess

def check_guess(guess): # checks if the user won
    if guess == answer():
        print("you got it!")
    else:
        check_letters(guess)

def check_letters(guess):
    for i in range(5):
        if guess[i] == answer()[i]:
            print(guess[i])