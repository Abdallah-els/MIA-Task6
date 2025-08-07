from Backend import *
from logic import *

counter = 0

while counter < 6:

    guess = user_guess()
    counter += 1

    if validating_user_word(guess) == 0:
        check_guess(guess)
    else:
        print("What's that? only 5-letters English words")

print("oh oh you lost")
