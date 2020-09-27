import pygame

from constants import SQUARE_SIZE
from board import Board


class Player:
    def __init__(self, color, board: Board):
        self.color = color
        self.board = board

    def on_click(self):
        column = self.board.get_column()

        self.add_piece(column)

    def add_piece(self, column):
        self.board.add_piece(column, self.color)
