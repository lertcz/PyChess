import pygame

class Board:
    def __init__(self, fen, display, pieces) -> None:
        self.fen = fen
        self.display = display
        self.light= (235, 195, 160)
        self.dark = (130, 95, 64)

        self.pieces = pieces

    def background(self):
        for file in range(8):
            for rank in range(8):
                if self.__IsBlackSquare(file, rank):
                    pygame.draw.rect(self.display, self.dark, (rank * 60, file * 60, 60, 60))
                else:
                    pygame.draw.rect(self.display, self.light, (rank * 60, file * 60, 60, 60))

    def __IsBlackSquare(self, x, y):
        return (x + y) % 2 != 0

    def decodeFEN(self):
        # rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR
        # self.display.blit(self.pieces["p"], (60, 0))
        file, rank = 0, 0
        for char in self.fen:
            if char == "/":
                file += 1
                rank = 0

            elif char.isdigit():
                rank += int(char)

            else:
                self.display.blit(self.pieces[char], (rank * 60, file * 60))
                rank += 1

            

    def draw(self):
        self.background()

        #will decode the FEN notation and add the pieces
        self.decodeFEN()

        pygame.display.flip()