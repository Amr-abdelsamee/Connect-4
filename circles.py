from matplotlib.pyplot import draw
import pygame

class Circle:
    def __init__(self, x_pos, y_pos, color, position_index, radius):
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.position_index = position_index
        self.radius = radius
        
    # draw used to draw the block
    def draw(self, screen):
        pygame.draw.circle(screen, self.color,(self.x_pos, self.y_pos), self.radius)
    
    # update used to update the block place called when exchange happens
    def update(self,color):
        self.color = color

    # check_clicked checks if the mouse click was on the block 
    def check_clicked(self, x_clicked , y_clicked):
        if( x_clicked >= self.x_pos 
        and x_clicked < self.x_pos + self.width
        and y_clicked >= self.y_pos
        and y_clicked < self.y_pos + self.height):
            return True
        
    
    # getters and setters for the class
    def get_label(self):
        return self.label
    
    def get_position(self):
        return self.position

    def get_x_pos(self):
        return self.x_pos
    
    def get_y_pos(self):
        return self.y_pos

    def set_x_pos(self, new_x_pos):
        self.x_pos = new_x_pos
    
    def set_y_pos(self, new_y_pos):
        self.y_pos = new_y_pos
    
    def set_position(self, new_position):
        self.position = new_position
