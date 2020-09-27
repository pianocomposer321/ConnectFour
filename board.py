import pygame

from piece import Piece
from constants import (
    ROWS,
    COLS,
    WHITE,
    SQUARE_SIZE,
    WIDTH,
    HEIGHT,
    TO_WIN
)


class Board:
    def __init__(self):
        self._board = [[None for _ in range(COLS)] for _ in range(ROWS)]

    def get_board(self):
        return self._board

    def get_column(self):
        x, _ = pygame.mouse.get_pos()
        return x // SQUARE_SIZE

    def get_pieces(self, piece, direction):
        if piece is None:
            return [None]

        pieces = [piece]
        row, col = piece.row, piece.col

        for i in range(1, TO_WIN):
            row += direction[0]
            col += direction[1]

            if row >= len(self._board) or col >= len(self._board[row]):
                pieces.append(None)
                continue

            pieces.append(self._board[row][col])

        return pieces

    def check_for_win(self, directions=((0, 1), (1, 1), (1, 0), (1, -1))):
        for row in self._board:
            for piece in row:
                for direction in directions:
                    pieces = self.get_pieces(piece, direction)
                    if all(pieces) and all(map(lambda x: x.color == piece.color, pieces)):
                        return True, piece.color
        return False, None

    def lowest_empty_space(self, column):
        for row in reversed(range(ROWS)):
            if self._board[row][column] is None:
                return (row, column)

    def add_piece(self, column, color):
        pos = self.lowest_empty_space(column)
        if pos:
            row, col = self.lowest_empty_space(column)
            self._board[row][col] = Piece(row, col, color)

    def draw(self, win: pygame.Surface):
        for x in range(1, COLS):
            start_pos = (x * SQUARE_SIZE, 0)
            end_pos = (x * SQUARE_SIZE, HEIGHT)

            pygame.draw.line(win, WHITE, start_pos, end_pos)

        for y in range(1, ROWS):
            start_pos = (0, y * SQUARE_SIZE)
            end_pos = (WIDTH, y * SQUARE_SIZE)
            pygame.draw.line(win, WHITE, start_pos, end_pos)

        for row in self._board:
            for piece in row:
                if piece is not None:
                    piece.draw(win)
