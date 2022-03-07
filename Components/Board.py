import pygame

class Board:
    def __init__(self, fen, display, pieces) -> None:
        self.BOARD = self.__loadFEN(fen)
        #[print(x) for x in self.BOARD]
        self.display = display
        self.pieces = pieces

        self.LIGHT= (235, 195, 160)
        self.DARK = (130, 95, 64)
        self.HIGHLIGHT = (246, 246, 105)

        self.holding = None

        self.pickupZone = None
        self.dropZone = None

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
            pygame.draw.rect(self.display, self.HIGHLIGHT, (rank * 60, file * 60, 60, 60))
        
        if self.dropZone:
            file, rank = self.dropZone
            pygame.draw.rect(self.display, self.HIGHLIGHT, (rank * 60, file * 60, 60, 60))

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
        return [x//60 for x in pygame.mouse.get_pos()]

    def pickup(self):
        rank, file = self.__ClickedSquarePosition()
        self.holding = self.BOARD[file][rank]
        if self.holding:
            self.BOARD[file][rank] = None

            self.pickupZone = [file, rank]
            self.dropZone = None

    def drop(self):
        rank, file = self.__ClickedSquarePosition()
        if self.holding:
            # replace the piece
            self.BOARD[file][rank] = self.holding
            # change status
            self.holding = None
            # change dropzone
            self.dropZone = [file, rank]

    def update(self):
        self.board()
        if self.holding:
            x, y = pygame.mouse.get_pos()
            self.display.blit(self.pieces[self.holding], (x - 30, y - 30))
        