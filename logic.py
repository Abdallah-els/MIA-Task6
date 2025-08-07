from Backend import *

def user_guess(): # takes the guesses
    guess = input("")
    return guess

def check_guess(guess): # checks if the user won
    if guess == answer():
        print("you got it!")
    else:
        check_exact_matches(guess)

def check_exact_matches(guess):
    exact_matches = ""
    for i in range(5):
        if guess[i] == answer()[i]:
            exact_matches += guess[i]
        else :
            exact_matches += "_"
    print(exact_matches)