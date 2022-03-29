import pygame
from puzzle import Puzzle


NUM_ROW = 10
NUM_COL = 8

# size constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = SCREEN_WIDTH

# back ground color constant
BGROUND_IMG = pygame.image.load("BG.jpg")


# starting the pygame screen
pygame.init()
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# draw the background 
game_screen.blit(BGROUND_IMG,(0,0))
# set the title
pygame.display.set_caption("Connect 4")
# set the logo
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)




puzzle = Puzzle(game_screen, NUM_ROW, NUM_COL, SCREEN_WIDTH, SCREEN_HEIGHT)

running = True # running condition

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # check if user clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            # store the coordinates of the clicked position
            x_clicked, y_clicked = pygame.mouse.get_pos()
            print(x_clicked, y_clicked)
        pygame.display.update()
pygame.quit()
