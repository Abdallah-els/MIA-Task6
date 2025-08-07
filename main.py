from Backend import *
from logic import *

counter = 0
answer = generate_answer()

while counter < 6:

    guess = user_guess()
    counter += 1

    if validating_user_word(guess) == True:

        if check_guess(guess,answer) == True:
            print("you got it!")

        else:
            colors = check_matches(guess,answer) # return list of colorss indicating each letter state
            processed_guess = color_answer(guess,colors)
            print (processed_guess)

    else:
        print("What's that? only 5-letters English words")

print("oh oh you lost")
print("correct answer was " + answer)
