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
        # self.clickable_ranges = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.num_row = num_row
        self.num_col = num_col
        
        # calculate the block width and height depending on the screen width and height
        self.diameter = (self.screen_width - (2 * SIDES_PADDING) - (
                    self.num_col * INBTWN_SPACE - 1)) / self.num_col
        print(self.diameter)

        self.create_circles()

# create_rects creates the blocks of the game
    def create_circles(self):
        # initial cordinates of the first block
        x = SIDES_PADDING + self.diameter/2
        y = UPPER_PADDING + self.diameter/2
        position = 0

        for _ in range(0, self.num_row):
            # self.clickable_ranges.append((x-self.diameter/2, y-self.diameter/2))
            for _ in range(0, self.num_col):
                circle = Circle(x, y, CIRCLE_COLOR, position, self.diameter/2)
                circle.draw(self.screen)
                self.circles.append(circle)
                x = x + self.diameter + INBTWN_SPACE
                position += 1
            x = SIDES_PADDING + self.diameter/2
            y = y + self.diameter + INBTWN_SPACE



    def get_col_clicked(self, x_clicked, y_clicked):
        last_circle_index = (self.num_col * self.num_row) -1
        y_end = self.circles[last_circle_index].y_pos + (self.diameter/2)
        print(y_end)
        for i in range(self.num_col):
            x_start = self.circles[i].x_pos - (self.diameter/2)
            x_end = self.circles[i].x_pos + (self.diameter/2)
            y_start = self.circles[i].y_pos - (self.diameter/2)
            if( x_clicked >= x_start
            and x_clicked < x_end
            and y_clicked >= y_start
            and y_clicked < y_end):
                return i

