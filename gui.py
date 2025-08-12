import pygame
from Backend import *
from logic import *

won = False
# answer = generate_answer()
answer = "happy"

# iniallizing pygame 
pygame.init()
WIDTH, HEIGHT = 450,600 # setting screen size
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("WORDLE by Elsherbiny") # caption

#setting background
background = pygame.image.load("gui files/bg.jpeg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

#setting "WORDLE"
WORDLE = pygame.image.load("gui files/WORDLE.png")
WORDLE = pygame.transform.scale(WORDLE, (350, 100))

#setting rectangles
rectangle = pygame.image.load("gui files/rect.jpeg")
rectangle = pygame.transform.scale(rectangle, (30, 40))

#settin font
font = pygame.font.Font(None, 50)
word = "" 

#processing the guess
def process(guess):
    global word
    global won
    
    if validating_user_word(guess) == True:

        if check_guess(guess,answer) == True: # user won

           won = True

        else:
            pass

    else:
        word = ""
            



# main
running = True
while running:
    for event in pygame.event.get(): # running throw each event happened in the loop to seaarch for exit
        if event.type == pygame.QUIT:
            running = False

        # taking input
        if event.type == pygame.KEYDOWN and not won:
            if event.key == pygame.K_BACKSPACE: # deleting character
                word = word[:-1]

            elif event.key == pygame.K_RETURN and len(word) == 5: # start processing after pressing enter
                process(word)

            elif len(word) < 5 and event.unicode.isalpha(): # only allowing letters
                word += event.unicode 

    screen.blit(background, (0, 0)) #display screen
    screen.blit(WORDLE, (50 , 15)) #display WORDLE

    #draw squares
    for i in range(6):
        for j in range(5):
            screen.blit(rectangle, (125 + 45*j , 120 + 65 * i))

    
    
    # showing the input
    if word:
        for i,letter in enumerate(word):

            # printing the input 
            text = font.render(letter, True, (255, 255, 255))
            screen.blit(text, (130 + 45 * i, 120))

    if won:

        winning_messege = "you got it!"
        text = font.render(winning_messege, True, (255, 255, 255))
        screen.blit(text, (140, 520))
        


    pygame.display.flip()

pygame.quit()


