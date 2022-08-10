#!/usr/bin/env python

import pygame
from pygame.locals import *
from chess_board import chess_board

WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 600

pygame.init()
display = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

running = True
chess_board = chess_board()

while running == True:
    
    display.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = not running
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                running = not running
    if not running:
        break;

    chess_board.draw(display)
    clock.tick(60)
    pygame.display.flip()

