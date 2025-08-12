import pygame

# iniallizing pygame 
pygame.init()
screen = pygame.display.set_mode((450, 600)) # setting screen size
pygame.display.set_caption("WORDLE by Elsherbiny")

running = True
while running:
    for event in pygame.event.get(): # running throw each event happened in the loop to seaarch for exit
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Fill screen with black
    pygame.display.flip()

pygame.quit()