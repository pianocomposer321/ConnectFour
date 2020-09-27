import pygame
from game import Game
from constants import WIDTH, HEIGHT

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connect 4")
game = Game(win)
game.run()
