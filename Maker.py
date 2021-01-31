import pygame
from pygame.locals import *


class button:
    def __init__(self, x, y, width, height, colour, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text

    def draw(self, surface):
        # surface is the window on which the rectangle should be drawn
        pygame.draw.rect(surface, self.colour, [self.x, self.y, self.width, self.height])

        if self.text != "":
            font = pygame.font.SysFont("Rockwell", 40)
            b_text = font.render(self.text, True, (255, 255, 255))
            x_coord = self.x + (self.width / 2 - b_text.get_width() / 2)
            y_coord = self.y + (self.height / 2 - b_text.get_height() / 2)
            surface.blit(b_text, (x_coord, y_coord))

    def mouse_over(self, pos):
        if self.x < pos[0] < (self.x + self.width):
            if self.y < pos[1] < (self.y + self.height):
                self.colour = (14, 77, 146)
                return True

    def mouse_click(self, pos):
        if self.mouse_over(pos):
            return True

    def colour_change(self, colour_type):
        if colour_type == "correct":
            self.colour = (76, 187, 23)
        elif colour_type == "wrong":
            self.colour = (255, 0, 0)
        elif colour_type == "normal":
            self.colour = (20, 20, 20)


# noinspection PyMethodMayBeStatic

class letter:
    def __init__(self, text):
        self.text = text
        self.font = pygame.font.SysFont("Rockwell", 30)
        if self.text != " ":
            self.colour = (30, 30, 30)
        else:
            self.colour = (255, 255, 255)
        self.to_draw = self.font.render(self.text, True, self.colour)

    def draw(self, surface, x, y):
        if self.text != " ":
            self.to_draw = self.font.render(self.text, True, self.colour)
            surface.blit(self.to_draw, (x, y))
        else:
            self.to_draw = self.font.render(self.text, True, self.colour)
            pygame.draw.rect(surface, self.colour, [x, y, self.get_info()[0], self.get_info()[1]])

    def set_colour(self, state):
        print(self.text, state)
        if self.text != " ":
            if state == "normal":
                self.colour = (30, 30, 30)
            elif state == "correct":
                self.colour = (76, 187, 23)
            elif state == "wrong":
                self.colour = (255, 0, 0)
        else:
            if state == "normal":
                self.colour = (255, 255, 255)
            elif state == "correct":
                self.colour = (190, 255, 148)
            elif state == "wrong":
                self.colour = (255, 102, 102)

    def get_info(self):
        width = self.to_draw.get_width()
        height = self.to_draw.get_height()
        return width, height

class text:
    def __init__(self, colour, x, y):
        self.colour = colour
        self.x, self.y = x, y

    def draw(self, text, surface):
        font = pygame.font.SysFont("Rockwell", 30)
        to_draw = font.render(text, True, self.colour)
        surface.blit(to_draw, (self.x, self.y))

