#!/usr/bin/env python

import pygame
from pygame.locals import *
from chess_board import chess_board

WINDOW_WIDTH  = 800
WINDOW_HEIGHT = 800

pygame.init()
display = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

running = True
chess_board = chess_board(WINDOW_WIDTH, WINDOW_HEIGHT)

dragging = False
selected = False
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = not running
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                running = not running
        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            row = chess_board.location_to_board_index(position[0])
            col = chess_board.location_to_board_index(position[1])
            selected = chess_board.get_piece_at_location((row,col))

            if not selected == False:
                selected.invisible = True
                chess_board.board[row][col] = False
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            row = chess_board.location_to_board_index(position[0])
            col = chess_board.location_to_board_index(position[1])
            selected.position = (row,col)
            chess_board.board[row][col] = selected
            selected.invisible = False
            dragging = False
            selected = False
    if not running:
        break;

    chess_board.draw(display)
    if dragging:
        loc = pygame.mouse.get_pos()
        display.blit(selected.image, loc)
    clock.tick(60)
    pygame.display.update()
