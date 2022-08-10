import pygame 
#from piece import pieces, piece

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

    def initialize_all_pieces(self):
        self.pieces = []
        from piece import pieces, piece
        #black pieces
        self.pieces.append(piece('black',pieces.tower,(0,0)))
        self.pieces.append(piece('black',pieces.horse,(1,0)))
        self.pieces.append(piece('black',pieces.rook,(2,0)))
        self.pieces.append(piece('black',pieces.king,(3,0)))
        self.pieces.append(piece('black',pieces.queen,(4,0)))
        self.pieces.append(piece('black',pieces.rook,(5,0)))
        self.pieces.append(piece('black',pieces.horse,(6,0)))
        self.pieces.append(piece('black',pieces.tower,(7,0)))
        
        self.pieces.append(piece('black',pieces.pawn,(0,1)))
        self.pieces.append(piece('black',pieces.pawn,(1,1)))
        self.pieces.append(piece('black',pieces.pawn,(2,1)))
        self.pieces.append(piece('black',pieces.pawn,(3,1)))
        self.pieces.append(piece('black',pieces.pawn,(4,1)))
        self.pieces.append(piece('black',pieces.pawn,(5,1)))
        self.pieces.append(piece('black',pieces.pawn,(6,1)))
        self.pieces.append(piece('black',pieces.pawn,(7,1)))

        #white pieces
        self.pieces.append(piece('white',pieces.tower,(0,7)))
        self.pieces.append(piece('white',pieces.horse,(1,7)))
        self.pieces.append(piece('white',pieces.rook,(2,7)))
        self.pieces.append(piece('white',pieces.king,(3,7)))
        self.pieces.append(piece('white',pieces.queen,(4,7)))
        self.pieces.append(piece('white',pieces.rook,(5,7)))
        self.pieces.append(piece('white',pieces.horse,(6,7)))
        self.pieces.append(piece('white',pieces.tower,(7,7)))

        self.pieces.append(piece('white',pieces.pawn,(0,6)))
        self.pieces.append(piece('white',pieces.pawn,(1,6)))
        self.pieces.append(piece('white',pieces.pawn,(2,6)))
        self.pieces.append(piece('white',pieces.pawn,(3,6)))
        self.pieces.append(piece('white',pieces.pawn,(4,6)))
        self.pieces.append(piece('white',pieces.pawn,(5,6)))
        self.pieces.append(piece('white',pieces.pawn,(6,6)))
        self.pieces.append(piece('white',pieces.pawn,(7,6)))

        for piece in self.pieces:
            self.board[piece.position[0]][piece.position[1]]= piece

    def draw_background(self,screen):
        square_width = self.width // 8
        square_height = square_width

        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                color = (255,255,255) if ((row % 2 == 0 and col % 2 == 0) or ((not row % 2 == 0) and (not col % 2 == 0))) else (0,0,0)
                cell_position = pygame.Rect(col * square_width, row * square_height, square_width, square_height)
                pygame.draw.rect(screen,color,cell_position)

    def location_to_board_index(self, location_in_pixels):
        return location_in_pixels // (self.width // 8)

    def draw_pieces(self, screen):
        for piece in self.pieces:
            piece.draw(screen)

    def get_piece_at_location(self, location):
        return self.board[location[0]][location[1]]
