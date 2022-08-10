
class chess_board():
    def __init__(self):
        self.board = [[False for x in range(21)] for y in range(21)]

    def draw(self, screen):
        print(self.board)

    def place_piece(self, piece):
        pass

    def initialize_all_pieces(self):
        pass
