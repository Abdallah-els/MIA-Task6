import random

def words():
    with open('words.txt', 'r') as database:
        lines =[word.strip() for word in database.readlines()] # makes a list of all words with out the /n
    return lines
            
def choose_answer():
    return random.choice(words()) #choose random word every time

def validating_user_word(guess): #return 0 when guess is correct and 1 when incorrect
    if guess in words():
        return 0
    else:
        return 1
