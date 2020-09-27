import pygame

from board import Board
from player import Player
from button import Button
from constants import (
    BLACK,
    RED,
    YELLOW,
    GREEN,
    WHITE,
    SQUARE_SIZE,
    ROWS,
    WIDTH,
    HEIGHT
)


class Game:
    PLAYING = 0
    HAS_WON = 1

    def __init__(self, win):
        self.win = win
        # self.running = True
        self.state = self.PLAYING
        self.running = True
        self.board = Board()

        self.players = [Player(RED, self.board), Player(YELLOW, self.board)]
        self.player_turn_counter = 0

        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 36)
        self.text = ""

        play_again_xpos = WIDTH // 5
        play_again_ypos = (HEIGHT // 5) * 4
        play_again_button = Button("Play Again",
                                   GREEN,
                                   self.play_again,
                                   xpos=play_again_xpos,
                                   ypos=play_again_ypos,
                                   show_border=True,
                                   border_color=(255, 255, 255))

        quit_xpos = (WIDTH // 5) * 4
        quit_ypos = (HEIGHT // 5) * 4
        quit_button = Button("Quit",
                             RED,
                             self.quit,
                             xpos=quit_xpos,
                             ypos=quit_ypos,
                             show_border=True,
                             border_color=(255, 255, 255))

        self.buttons = [play_again_button, quit_button]

    def play_again(self):
        self.__init__(self.win)
        self.run()

    def quit(self):
        self.running = False

    def draw(self):
        self.win.fill(BLACK)
        self.board.draw(self.win)
        if self.state == self.HAS_WON:
            # self.win.fill(WHITE)
            text = self.font.render(self.text, True, WHITE)

            text_rect = text.get_rect()
            text_rect.centerx = WIDTH // 2
            text_rect.centery = ((SQUARE_SIZE * ROWS) // 3) - SQUARE_SIZE // 2

            self.win.blit(text, text_rect)

            for button in self.buttons:
                button.draw(self.win)
            # self.play_again_button.draw(self.win)
            # self.quit_button.draw(self.win)

        pygame.display.update()

    def is_full(self, column):
        board = self.board.get_board()
        # pieces = []

        # for row in board:
        #     pieces.append(row[column])

        # return all(pieces)
        return all([row[column] for row in board])

    def on_win(self, color):
        self.state = self.HAS_WON
        colors = {(255, 255, 0): "Yellow", (255, 0, 0): "Red"}
        self.text = f"{colors[color]} has won!"
        # print(f"{colors[color]} has won!")

    def on_click(self):
        if self.state == self.PLAYING:
            column = self.board.get_column()
            if not self.is_full(column):
                self.player_turn_counter += 1
                self.player_turn_counter = self.player_turn_counter % 2
            self.players[self.player_turn_counter].on_click()
            has_won, color = self.board.check_for_win()
            if has_won:
                self.on_win(color)
        elif self.state == self.HAS_WON:
            for button in self.buttons:
                button.on_click()

    def run(self):
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_click()

            self.draw()
