import pygame
from Components.Board import Board

startFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
board = Board(startFEN)

# Images ----------------
""" bBishop = pygame.image.load("Assets/Pieces/bBishop.png")
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
wRook = pygame.image.load("Assets/Pieces/wRook.png") """

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        """ elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: # lmb
                board.pickup()

        elif event.type == pygame.MOUSEBUTTONUP:
            board.drop()
            board.board
    
    board.update()
    pygame.display.flip() """