from Backend import *

def check_guess(guess,answer): # checks if the user won

    if guess == answer:
        return True
    else:
        return False


def check_matches(guess,answer): # return list of colorss indicating each letter state

    ans = answer
    exact_matches = ""
    worng_matches = {}
    colors = ["grey" , "grey" , "grey" , "grey" ,"grey"] # default color all letters white

    for i in range(5): # checks the letters 1 by 1 to see which letter is in its exact position
        if guess[i] == ans[i]:
            exact_matches += guess[i]
            colors[i] = "green" # change color of correct letters to green
        else :
            exact_matches += "_"
            worng_matches[i] = guess[i] # key: index, value: letter
    
    for key , value in worng_matches.items(): #checks correct letters in wrong position
        for i in range(5):
            if value == ans[i] and value != exact_matches[i]:
                colors[key] = "yellow"
                ans = ans[:i] + "-" + ans[i+1:] # removing checked letter to prevent letter repeating bug

    return colors


def color_answer(guess,colors): # combine the guess with the colors

    colored_word = ""
    for i, char in enumerate(guess):
        colored_word += colors[i] + char
    colored_word += "grey"

    return colored_word