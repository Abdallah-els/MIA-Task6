import pygame

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
input_text = "" 

running = True
while running:
    for event in pygame.event.get(): # running throw each event happened in the loop to seaarch for exit
        if event.type == pygame.QUIT:
            running = False
        # taking input
        elif event.type == pygame.KEYDOWN:
            input_text += event.unicode 

    screen.blit(background, (0, 0)) #display screen
    screen.blit(WORDLE, (50 , 15)) #display WORDLE

    #draw squares
    for i in range(6):
        for j in range(5):
            screen.blit(rectangle, (125 + 45*j , 120 + 65 * i))

    
    
    # showing the input
    word = input_text
    if word:
        for i,letter in enumerate(word):
            # printing the output 
            text = font.render(letter, True, (255, 255, 255))
            screen.blit(text, (130 + 45 * i, 120))

            if len(word) == 5:
                pass
                



    pygame.display.flip()

pygame.quit()
