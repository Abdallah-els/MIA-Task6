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


running = True
while running:
    for event in pygame.event.get(): # running throw each event happened in the loop to seaarch for exit
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0)) #display screen
    screen.blit(WORDLE, (50 , 15)) #display WORDLE

    #draw squares
    for i in range(6):
        for j in range(5):
            screen.blit(rectangle, (125 + 45*j , 120 + 65 * i))
            # pygame.draw.rect(screen, (0, 0, 255), (110 + 50*j , 120 + 65 * i, 30, 40)) #(x, y, width, height)


    pygame.display.flip()

pygame.quit()