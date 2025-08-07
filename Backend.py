import random

def read_database():
    with open('words.txt', 'r') as database:
        words =[word.strip() for word in database.readlines()] # makes a list of all words with out the /n
    return words
            
def choose_answer():
    return random.choice(read_database()) #choose random word every time

def validating_user_word(guess): #return 0 when guess is correct and 1 when incorrect
    if guess in read_database():
        return 0
    else:
        return 1


