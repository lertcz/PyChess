import pygame

pygame.mixer.init()
pygame.mixer.music.load("Assets/Sounds/move.mp3")
pygame.mixer.music.set_volume(0.7)

#setup of a highlight square
highlightSquare = pygame.Surface((60,60))
highlightSquare.set_alpha(128) # alpha level
highlightSquare.fill((246, 246, 105))  

#setup of a possible move square
possibleMoveSquare = pygame.Surface((60,60))
possibleMoveSquare.set_alpha(128) # alpha level
possibleMoveSquare.fill((255, 0, 0))  

class Board:
    color = {
        "b": -1,
        "w": 1
    }
    def __init__(self, fen, display, pieces) -> None:
        self.BOARD = self.__loadFEN(fen)
        #[print(x) for x in self.BOARD]
        self.display = display
        self.pieces = pieces

        self.LIGHT= (235, 195, 160)
        self.DARK = (130, 95, 64)
        #self.HIGHLIGHT = (246, 246, 105)

        self.holding = None

        self.pickupZone = None
        self.dropZone = None
        self.legal_moves = []

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
        
    def board(self):
        self.background()
        self.highlighted()
        self.displayPieces()

    def highlighted(self):
        if self.pickupZone:
            file, rank = self.pickupZone
            self.display.blit(highlightSquare, (rank * 60, file * 60))
        
        if self.dropZone:
            file, rank = self.dropZone
            self.display.blit(highlightSquare, (rank * 60, file * 60))

        if self.holding:
            self.legalMoves()
            for square in self.legal_moves:
                file, rank = square
                self.display.blit(possibleMoveSquare, (rank * 60, file * 60))

    def legalMoves(self):
        if not self.legal_moves:
            y, x = self.pickupZone
            if self.holding.lower() == "p":
                self.pawnMove(x, y)

            elif self.holding.lower() == "b":
                self.bishopMove(x, y)
            
            elif self.holding.lower() == "n":
                self.knightMove(x, y)

            elif self.holding.lower() == "r":
                self.rookMove(x, y)

            elif self.holding.lower() == "k":
                self.kingMove(x, y)

            elif self.holding.lower() == "q":
                self.queeenMove(x, y)

    def pawnMove(self, x , y):
        color = "b" if self.holding.isupper() else "w"
        orientation = self.color[color]
        
        #!TODO promotion

        #!TODO start move by 2

        # base move
        if 0 <= y + orientation <= 7: # boundary check
            if not self.BOARD[y + orientation][x]: # only move if nothing is in front
                self.legal_moves.append([y + orientation, x])

        # elimination
        # condition to take care of overflow
        for side in [-1, 1]:
            if 0 <= x + side <= 7 and 0 <= y + orientation <= 7: # boundary check
                # if there is a piece on the side and it is an enemy
                if self.BOARD[y + orientation][x + side] and self.__checkEnemyPiece(color, x + side, y + orientation):
                    self.legal_moves.append([y + orientation, x + side])

    def __checkEnemyPiece(self, side, x, y):
        if side == "b":
            return self.BOARD[y][x].islower()
        return self.BOARD[y][x].isupper()

    def straightLine(self, side, x, y):
        for X in [-1, 1]:
            temp = x
            while 0 <= temp <= 7:
                if temp != x: #not self
                    if self.BOARD[y][temp]: # stop after finding a piece
                        if self.__checkEnemyPiece(side, temp, y): # add enemy piece to be eliminated
                            self.legal_moves.append([y, temp])
                        break

                    self.legal_moves.append([y, temp])
                temp += X
            
        for Y in [-1, 1]:
            temp = y
            while 0 <= temp <= 7:
                if temp != y: #not self
                    if self.BOARD[temp][x]: # stop after finding a piece
                        if self.__checkEnemyPiece(side, x, temp): # add enemy piece to be eliminated
                            self.legal_moves.append([temp, x])
                        break

                    self.legal_moves.append([temp, x])
                temp += Y

    def __checkEnemyPieceDiagonal(self, side, MAIN, temp, x, y):
        if side == "b":
            return self.BOARD[y + temp][x + (temp * MAIN)].islower()
        return self.BOARD[y + temp][x + (temp * MAIN)].isupper()

    def diagonalLine(self, side, x, y):
        for DIAGONAL in [-1, 1]:
            for MAIN in [-1, 1]:
                temp = 0
                while 0 <= x + (temp * MAIN) <= 7 and 0 <= y + temp <= 7:
                    if temp != 0: #not self
                        if self.BOARD[y + temp][x + (temp * MAIN)]: # stop after finding a piece
                            if self.__checkEnemyPieceDiagonal(side, MAIN, temp, x, y): # add enemy piece to be eliminated
                                self.legal_moves.append([y + temp, x + (temp * MAIN)])
                            break

                        self.legal_moves.append([y + temp, x + (temp * MAIN)])
                    temp += DIAGONAL

    def bishopMove(self, x ,y):
        color = "b" if self.holding.isupper() else "w"

        self.diagonalLine(color, x, y)
    
    def knightMove(self, x ,y):
        color = "b" if self.holding.isupper() else "w"

        for X in [1, -1, 2, -2]:
            for Y in [1, -1, 2, -2]:
                if X != Y and X != -Y:
                    if 0 <= x+X <= 7 and 0 <= y+Y <= 7:
                        #check for enemy
                        if self.BOARD[y+Y][x+X]: 
                            if self.__checkEnemyPiece(color, x + X, y + Y):
                                self.legal_moves.append([y + Y, x + X])
                        #check for free space
                        else:
                            self.legal_moves.append([y + Y, x + X])
    
    def rookMove(self, x ,y):
        color = "b" if self.holding.isupper() else "w"

        self.straightLine(color, x, y)
    
    def kingMove(self, x ,y):
        color = "b" if self.holding.isupper() else "w"

        for Y in range(-1, 2):
            for X in range(-1, 2):
                if X or Y != 0: # not it self
                    if 0 <= x+X <= 7 and 0 <= y+Y <= 7:
                        #check for enemy
                        if self.BOARD[y+Y][x+X]: 
                            if self.__checkEnemyPiece(color, x + X, y + Y):
                                self.legal_moves.append([y + Y, x + X])
                        #check for free space
                        else:
                            self.legal_moves.append([y + Y, x + X])
    
    def queeenMove(self, x ,y):
        color = "b" if self.holding.isupper() else "w"

        self.straightLine(color, x, y)
        self.diagonalLine(color, x, y)

    def background(self):
        for file in range(8):
            for rank in range(8):
                if self.__IsBlackSquare(file, rank):
                    pygame.draw.rect(self.display, self.DARK, (rank * 60, file * 60, 60, 60))
                else:
                    pygame.draw.rect(self.display, self.LIGHT, (rank * 60, file * 60, 60, 60))

    def __IsBlackSquare(self, x, y):
        return (x + y) % 2 != 0
    
    def displayPieces(self):
        for y in range(8):
            for x in range(8):
                if self.BOARD[y][x]:
                    currentPiece = self.BOARD[y][x]
                    self.display.blit(self.pieces[currentPiece], (x * 60, y * 60))

    def __ClickedSquarePosition(self):
        return [x//60 for x in pygame.mouse.get_pos()][::-1]

    def pickup(self):
        file, rank = self.__ClickedSquarePosition()
        self.holding = self.BOARD[file][rank]
        if self.holding:
            self.BOARD[file][rank] = None

            self.pickupZone = [file, rank]
            self.dropZone = None

    def drop(self):
        file, rank = self.__ClickedSquarePosition()
        if self.holding:
            if [file, rank] in self.legal_moves and self.__ClickedSquarePosition() != self.pickupZone:
                # replace the piece
                self.BOARD[file][rank] = self.holding
                # change status
                self.holding = None
                # change dropzone and clear legal_move list
                self.dropZone = [file, rank]
                # play the sound if u chose valid square
                pygame.mixer.music.play()
            else:
                # choose last position
                file, rank = self.pickupZone
                self.BOARD[file][rank] = self.holding
                self.holding = None
            
            self.legal_moves.clear()

    def update(self):
        self.board()
        if self.holding:
            x, y = pygame.mouse.get_pos()
            self.display.blit(self.pieces[self.holding], (x - 30, y - 30))
        