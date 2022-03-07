import pygame, os
from Components.Board import Board


# INTI ------------------
pygame.init()

# board is 60px * 8
display_width = 480
display_height = 480

# set window size
gameDisplay = pygame.display.set_mode((display_width,display_height))
# set window name
pygame.display.set_caption('Chess')
# set window icon
Icon = pygame.image.load('Pieces/bQueen.png')
pygame.display.set_icon(Icon)


# Images ----------------
bBishop = pygame.image.load("Pieces/bBishop.png")
bKing = pygame.image.load("Pieces/bKing.png")
bKnight = pygame.image.load("Pieces/bKnight.png")
bPawn = pygame.image.load("Pieces/bPawn.png")
bQueen = pygame.image.load("Pieces/bQueen.png")
bRook = pygame.image.load("Pieces/bRook.png")
wBishop = pygame.image.load("Pieces/wBishop.png")
wKing = pygame.image.load("Pieces/wKing.png")
wKnight = pygame.image.load("Pieces/wKnight.png")
wPawn = pygame.image.load("Pieces/wPawn.png")
wQueen = pygame.image.load("Pieces/wQueen.png")
wRook = pygame.image.load("Pieces/wRook.png")

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
            board.board
    
    board.update()
    pygame.display.flip()
