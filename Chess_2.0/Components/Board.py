import pygame

# INIT ------------------
pygame.init()

# board is px * cells
display_width = 60 * 8
display_height = 60 * 8

# set window size
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Chess')
Icon = pygame.image.load('Assets/Pieces/bQueen.png')
pygame.display.set_icon(Icon)

class Board:
    def __init__(self, _FEN) -> None:
        self.BOARD = self.__loadFEN(_FEN)
    
    def __loadFEN(self, fen):
        board = []
        temp = []

        for char in fen:
            if char == "/":
                board.append(temp)
                temp = []

            elif char.isdigit():
                for _ in range(int(char)):
                    temp.append(None)

            else:
                temp += char

        board.append(temp)
        return board