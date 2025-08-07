from Backend import *
from logic import *

guess = user_guess()

if validating_user_word(guess) == 0:
    check_guess(guess)
else:
    pass
