import pygame

from constants import SQUARE_SIZE


class Piece:
    def __init__(self, row: int, column: int, color: tuple):
        self.row, self.col = row, column
        self.radius = SQUARE_SIZE // 2
        self.color = color

    def get_pos(self):
        pass

    def calculate_position(self):
        pos_x = (self.col * SQUARE_SIZE + self.radius) + 1
        pos_y = (self.row * SQUARE_SIZE + self.radius) + 1
        return (pos_x, pos_y)

    def draw(self, win: pygame.Surface):
        pos = self.calculate_position()

        pygame.draw.circle(win, self.color, pos, self.radius)
