from enum import Enum
import pygame

class pieces(Enum):
    tower = 0
    horse = 1
    rook = 2
    king = 3
    queen = 4
    pawn = 5

class piece():
    def __init__(self,color,piece_type,position):
        self.piece_type = piece_type
        self.color = color
        self.image = pygame.image.load(self.get_image_location(self.piece_type))
        self.image = pygame.transform.scale(self.image, (800 // 8, 800 // 8))
        self.position = position
        self.invisible = False

    def get_image_location(self,piece_type):
        if type(piece_type) == pieces:
            return "./"+ piece_type.name+"_"+str(self.color)+".png"
        else:
            print('error, make sure piece type is of type pieces')

    def draw(self, screen):
        if not self.invisible:
            screen.blit(self.image, (self.position[0] * (800 // 8), self.position[1] * (800 // 8)))
        else:
            pass
