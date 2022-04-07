import pygame
from puzzle import Puzzle
from buttons import Button
import time


NUM_ROW = 10
NUM_COL = 8

# size constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = SCREEN_WIDTH
SIDES_PADDING = 10
INBTWN_SPACE = 1
PUZZLE_WIDTH = (SCREEN_WIDTH - (2*SIDES_PADDING))

# properties of buttons
# TEXT_COLOR = (150,150,150)
TEXT_COLOR = (255,255,255)
BUTTONS_COLOR = (12,44,130)
BUTTON_WIDTH = 400
BUTTON_HEIGHT = 100
FONT_SIZE1 = 50
FONT_SIZE2 = 30

# back ground color constant
BGROUND_IMG = pygame.image.load("BG.jpg")

# windows variables
# players_mode checks if player or AI
players_mode = True
# ai_mode store the selected agent  
ai_mode = None
# A_star_type store the heurestic type

# start window contains two buttons play and AI
def start_window():
    global players_mode
    buttons = []
    player_button = Button((SCREEN_WIDTH//2)-(BUTTON_WIDTH//2), (SCREEN_HEIGHT//2)-(BUTTON_HEIGHT//2)-100, BUTTON_WIDTH,BUTTON_HEIGHT,BUTTONS_COLOR," Play",TEXT_COLOR,FONT_SIZE1)
    player_button.draw(game_screen)
    buttons.append(player_button)
    AI_button = Button((SCREEN_WIDTH//2)-(BUTTON_WIDTH//2), (SCREEN_HEIGHT//2)-(BUTTON_HEIGHT//2)-100 + 50 + BUTTON_HEIGHT + SIDES_PADDING, BUTTON_WIDTH,BUTTON_HEIGHT,BUTTONS_COLOR," AI",TEXT_COLOR,FONT_SIZE1)
    AI_button.draw(game_screen)
    buttons.append(AI_button)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_clicked,y_clicked = pygame.mouse.get_pos()
                
                for i in range(len(buttons)):
                    if buttons[i].check_clicked(x_clicked, y_clicked):
                        if i == 0:
                            players_mode = True
                            return
                        if i == 1:
                            return
                
            pygame.display.update()
    pygame.quit()

# AI window contains three buttons BFS DFS A*
def AI_window():
    game_screen.blit(BGROUND_IMG,(0,0))
    global ai_mode
    buttons = []
    BFS = Button((SCREEN_WIDTH//2)-(BUTTON_WIDTH//2), (SCREEN_HEIGHT//2)-(BUTTON_HEIGHT//2)-100, BUTTON_WIDTH,BUTTON_HEIGHT,BUTTONS_COLOR," BFS",TEXT_COLOR,FONT_SIZE1)
    BFS.draw(game_screen)
    buttons.append(BFS)
    DFS = Button((SCREEN_WIDTH//2)-(BUTTON_WIDTH//2), (SCREEN_HEIGHT//2)-(BUTTON_HEIGHT//2)-100 + BUTTON_HEIGHT + SIDES_PADDING, BUTTON_WIDTH,BUTTON_HEIGHT,BUTTONS_COLOR," DFS",TEXT_COLOR,FONT_SIZE1)
    DFS.draw(game_screen)
    buttons.append(DFS)
    a_star = Button((SCREEN_WIDTH//2)-(BUTTON_WIDTH//2), (SCREEN_HEIGHT//2)-(BUTTON_HEIGHT//2)-100 + (2*BUTTON_HEIGHT) + (2*SIDES_PADDING), BUTTON_WIDTH,BUTTON_HEIGHT,BUTTONS_COLOR," A*",TEXT_COLOR,FONT_SIZE1)
    a_star.draw(game_screen)
    buttons.append(a_star)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_clicked,y_clicked = pygame.mouse.get_pos()
                for i in range(len(buttons)):
                    if buttons[i].check_clicked(x_clicked, y_clicked):
                        if i == 0:
                            ai_mode = 0
                            return
                        if i == 1:
                            ai_mode = 1
                            return
                        if i == 2:
                            ai_mode = 2
                            return
                
            pygame.display.update()
    pygame.quit()


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



# start_window()
if players_mode:
    # draw the background again for the new window
    game_screen.blit(BGROUND_IMG,(0,0))
    # create a ppuzzle object
    puzzle = Puzzle(game_screen, NUM_ROW, NUM_COL, SCREEN_WIDTH, SCREEN_HEIGHT)
    
    running = True # running condition
    solved = False # solved condition
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # check if user clicked
            if event.type == pygame.MOUSEBUTTONDOWN and not solved:
                # store the coordinates of the clicked position
                x_clicked, y_clicked = pygame.mouse.get_pos()
                print(x_clicked, y_clicked)
            pygame.display.update()
    pygame.quit()


else:
    AI_window()
    # draw the background again for the new window
    game_screen.blit(BGROUND_IMG,(0,0))
    
    if ai_mode != None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()

