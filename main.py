from tkinter import *
from PIL import ImageTk, Image
import pygame
import sys
from puzzle import Puzzle
from circles import Circle
from tree import Tree
from copy import copy

NUM_ROW = 6
NUM_COL = 7

# size constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = SCREEN_WIDTH + 50

WHITE = (255, 255, 255)
BG_COLOR = WHITE
# back ground color constant
# BGROUND_IMG = pygame.image.load("BG.jpg")

pygame.init()

def message(image_name):
    tree_screen = Tk()
    tree_screen.title("State Tree")
    tree_image = Image.open(image_name)
    tkimage = ImageTk.PhotoImage(tree_image)
    image_height = tkimage.height()
    image_width = tkimage.width()

    tree_screen.geometry(str(image_width) + "x" + str(image_height))
    frame = Frame(tree_screen, width = image_width, height = image_height)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    frame.pack()
    img = ImageTk.PhotoImage(tree_image)
    label = Label(frame, image = img)
    label.pack()
    tree_screen.update()
    tree_screen.deiconify()
    tree_screen.mainloop()


def tree_window(states):
    # states = [["1",["1st_state_child1","1st_state_child2","1st_state_child3","1st_state_child4"]],
    #         ["2",["2nd_state_child1","2nd_state_child2","2nd_state_child3","2nd_state_child4"]],
    #         ["3",["3rd_state_child"]],
    #         ["4",["4th_state_child1","4th_state_child3","4th_state_child4"]],
    #         ["1st_state_child2",["5th_state_child1","4th_state_child3"]],
    #         ["6",["6th_state_child1","4th_state_child3"]],
    #         ["7",["7th_state_child1","4th_state_child3"]]
    #         ]
    tree = Tree(states, NUM_COL, NUM_ROW)
    image_name = tree.png_name +'.'+tree.extension
    message(image_name)


# starting the pygame screen
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# draw the background 
game_screen.fill(BG_COLOR)
# game_screen.blit(BGROUND_IMG,(0,0))
# set the title
pygame.display.set_caption("Connect 4")
# set the logo
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)




puzzle = Puzzle(game_screen, NUM_ROW, NUM_COL, SCREEN_WIDTH, SCREEN_HEIGHT)

playing_circle = Circle(game_screen, puzzle.circles[0].x_pos, puzzle.circles[0].y_pos - puzzle.diameter-10, puzzle.player1_color, puzzle.diameter/2)
playing_circle.draw()

running = True # running condition
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            x_hovered, y_hovered = pygame.mouse.get_pos()
            clear_rect = pygame.Rect(0, 0, SCREEN_WIDTH, 140)
            pygame.draw.rect(game_screen, BG_COLOR, clear_rect)
            playing_circle.change_pos(x_hovered, puzzle.circles[0].y_pos - puzzle.diameter-10)
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            # store the coordinates of the clicked position
            x_clicked, y_clicked = pygame.mouse.get_pos()
            
            puzzle.play(x_clicked , y_clicked)
            if puzzle.player_turn == '2': playing_circle.update(puzzle.player2_color, '0')
            else: playing_circle.update(puzzle.player1_color, '0')
            pygame.display.update()
            # if puzzle.player_turn == '1': tree_window(copy(puzzle.states))

        pygame.display.update()
