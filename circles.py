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

