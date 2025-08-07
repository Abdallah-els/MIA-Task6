from Backend import *

def user_guess(): # takes the guesses
    guess = input("")
    return guess

def check_guess(guess): # checks if the user won
    if guess == answer():
        print("you got it!")
    else:
        check_matches(guess)

def check_matches(guess): 
    exact_matches = ""
    worng_matches = []
    wrong_position = ""

    for i in range(5): # checks the letters 1 by 1 to see which letter is in its exact position
        if guess[i] == answer()[i]:
            exact_matches += guess[i]
        else :
            exact_matches += "_"
            worng_matches.append(guess[i])
    
    for letter in worng_matches: #checks correct letters in wrong position
        for i in range(5):
            if letter == answer()[i] and letter != exact_matches[i]:
                wrong_position += letter
                wrong_position += " - "


    print(exact_matches + " - correct letters but wrong position: " + wrong_position)

    

