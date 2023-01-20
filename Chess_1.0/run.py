import pygame, os
from Components.Board import Board


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


# Images ----------------
bBishop = pygame.image.load("Assets/Pieces/bBishop.png")
bKing = pygame.image.load("Assets/Pieces/bKing.png")
bKnight = pygame.image.load("Assets/Pieces/bKnight.png")
bPawn = pygame.image.load("Assets/Pieces/bPawn.png")
bQueen = pygame.image.load("Assets/Pieces/bQueen.png")
bRook = pygame.image.load("Assets/Pieces/bRook.png")
wBishop = pygame.image.load("Assets/Pieces/wBishop.png")
wKing = pygame.image.load("Assets/Pieces/wKing.png")
wKnight = pygame.image.load("Assets/Pieces/wKnight.png")
wPawn = pygame.image.load("Assets/Pieces/wPawn.png")
wQueen = pygame.image.load("Assets/Pieces/wQueen.png")
wRook = pygame.image.load("Assets/Pieces/wRook.png")

ImageLocation = {
    "b" : bBishop,
    "k" : bKing,
    "n" : bKnight,
    "p" : bPawn,
    "q" : bQueen,
    "r" : bRook,
    "B" : wBishop,
    "K" : wKing,
    "N" : wKnight,
    "P" : wPawn,
    "Q" : wQueen,
    "R" : wRook,
}


# VARIABLES -------------
#startFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
startFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

board = Board(startFEN, gameDisplay, ImageLocation)

#init the board
board.board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: # lmb
                board.pickup()

        elif event.type == pygame.MOUSEBUTTONUP:
            board.drop()
    
    board.update()
    pygame.display.flip()
