from copy import copy

from circles import Circle

# screen constants
SIDES_PADDING = 10
UPPER_PADDING = 100
LOWER_PADDING = 20
INBTWN_SPACE = 1

# blocks constants
CIRCLE_COLOR = (15,10,50)


class Puzzle:

    def __init__(self, screen, num_row, num_col, screen_width, screen_height):
        self.screen = screen

        self.circles = [] # array of obj
        self.playable = [] # array of ints
        self.occupied = [] # array of ints

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.num_row = num_row
        self.num_col = num_col
        
        # calculate the block width and height depending on the screen width and height
        self.diameter = (self.screen_width - (2 * SIDES_PADDING) - (
                    self.num_row * INBTWN_SPACE - 1)) / self.num_row
        print(self.diameter)

        self.create_circles()

# create_rects creates the blocks of the game
    def create_circles(self):
        # initial cordinates of the first block
        x = SIDES_PADDING + self.diameter/2
        y = UPPER_PADDING + self.diameter/2
        position = 0

        for _ in range(0, self.num_col):
            for _ in range(0, self.num_row):
                circle = Circle(x, y, CIRCLE_COLOR, position, self.diameter/2)
                circle.draw(self.screen)
                self.circles.append(circle)
                x = x + self.diameter + INBTWN_SPACE
                position += 1
            x = SIDES_PADDING + self.diameter/2
            y = y + self.diameter + INBTWN_SPACE





