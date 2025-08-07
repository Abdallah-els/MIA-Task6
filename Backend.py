import random

def words():
    with open('words.txt', 'r') as database:
        lines =[word.strip() for word in database.readlines()] # makes a list of all words with out the /n
    return lines
            
def generate_answer():

    return random.choice(words()) #choose random word every time


def validating_user_word(guess): #return True when guess is correct and False when incorrect
    if guess in words():
        return True
    else:
        return False
