import pygame 

class chess_board():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.board = [[False for x in range(21)] for y in range(21)]
        self.initialize_all_pieces()

    def draw(self, screen):
        screen.fill((0,0,0))
        self.draw_background(screen)
        self.draw_pieces(screen)

    def place_piece(self, piece):
        pass

    def initialize_all_pieces(self):
        pass

    def draw_background(self,screen):
        square_width = self.width // 8
        square_height = square_width

        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                color = (255,255,255) if ((row % 2 == 0 and col % 2 == 0) or ((not row % 2 == 0) and (not col % 2 == 0))) else (0,0,0)
                cell_position = pygame.Rect(col * square_width, row * square_height, square_width, square_height)
                pygame.draw.rect(screen,color,cell_position)

    def draw_pieces(self, screen):
        pass
